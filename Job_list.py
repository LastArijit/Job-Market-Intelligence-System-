# IMPORTING LIBRARIES

import requests as rq
import pandas as pd
import sqlite3 as sql
import os
import re
from dotenv import load_dotenv
import subprocess

# Load environment variables
load_dotenv()

# requests → used to call the API (fetch data from internet)
# pandas → used to organize data into a table and save as CSV
# Sqlite3 → used to connect to a SQL database

#-----------------------------------------------------------------------------------
# API DATA EXTRACTION

# url part
url = "https://jsearch.p.rapidapi.com/search"
# Broad query to fetch mixed jobs from India
query = "latest jobs India"

#parameters
querystring = {
    "query": query,
    "page": "1",
    "num_pages": "1"
}

#Authentication
headers = {
    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = rq.get(url, headers = headers, params = querystring)
if response.status_code == 200:
    data = response.json()

    jobs = data.get('data', [])
    if len(jobs) == 0:
        print ('Empty response')

else:
    print(f"Error: {response.status_code}")
    exit()

#precausion for data extraction
if 'data' in data:
    jobs = data['data']
else:
    print("Error in API response:", data)
    exit()

#-----------------------------------------------------------------------------
# TRANSFORM RAW DATA STRUCTURE + CREATE DATAFRAME

job_list = []

for job in jobs:
    job_info = {
        "title": job.get("job_title"),
        "company": job.get("employer_name"),
        "location": job.get("job_city") or job.get("job_location"),
        "job_type": job.get("job_employment_type"),
        "salary": job.get("job_salary") or job.get("job_salary_string") or "Not Disclosed",
        "job_url": job.get("job_apply_link"),
        "posted_date": job.get("job_posted_at_datetime_utc") or job.get("job_posted_at") or "Not Available",
        "work_mode": (
            "Remote" if job.get("job_is_remote") is True
            else "On-site" if job.get("job_is_remote") is False
            else "Hybrid"
        )
    }

    job_list.append(job_info)

# Convert list TO DataFrame
df = pd.DataFrame(job_list)
df = df.head(20)

#-------------------------------------------------------------------------------------------
# DATA CLEANING

#Drop rows where critical fields are missing
df = df.dropna(subset=['title', 'job_url'])

#remove tracking parameters from URL
df['job_url'] = df['job_url'].apply(
    lambda url: url if pd.isna(url) else url.split("?")[0]
)

# Handling missing values
df['company'] = df['company'].fillna("Unknown")
df['location'] = df['location'].fillna("India")
df['location'] = df['location'].apply(
    lambda loc: next((part.strip() for part in str(loc).split(",") if part.strip().lower() != "india"),"India"))
df['posted_date'] = df['posted_date'].fillna("Not Available")
df['job_type'] = df['job_type'].fillna('Unknown')

#Standardizing title, company, location
df['company'] = df['company'].str.strip().str.title()
df['location'] = df['location'].str.strip().str.title()

#Adding columns for clarity on the title
from mappings import ROLE_MAP, DOMAIN_MAP, LEVEL_MAP

def normalize_title_text(value):
    text = str(value).lower()
    text = text.replace("&", " and ")
    text = text.replace("/", " ")
    text = text.replace("|", " ")
    text = text.replace("-", " ")
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def standardize_title(title):
    normalized_title = normalize_title_text(title)

    for key, value in ROLE_MAP.items():
        if normalize_title_text(key) in normalized_title:
            return value

    return str(title).strip().title()


def detect_level(title):
    normalized_title = normalize_title_text(title)

    for level, keywords in LEVEL_MAP:
        for keyword in keywords:
            if normalize_title_text(keyword) in normalized_title:
                return level

    return "Not Specified"


def extract_features(title):
    title_clean = standardize_title(title)

    level = detect_level(title)
    domain = DOMAIN_MAP.get(title_clean, "General")

    return pd.Series([level, domain, title_clean])

# Add the columns
df[['level', 'domain', 'clean_title']] = df['title'].apply(extract_features)
from ai_implementation import process_general_domains
df = process_general_domains(df)
#------------------------------------------------------------------------------------------------
# Connect to sqlite database + Append data from dataframe to job.db

# Connect to existing database
conn = sql.connect("job_search.db")
cursor = conn.cursor()

# Step 1: Fetch existing job URLs from DB
cursor.execute("SELECT job_url FROM jobs")
existing_urls = {row[0] for row in cursor.fetchall()}

# Step 2: Filter DataFrame (remove duplicates)
df = df[~df['job_url'].isin(existing_urls)]

# Optional safety: remove duplicates inside DataFrame itself
df = df.drop_duplicates(subset=['job_url'])

# Step 3: Insert only new data
if not df.empty:
    df.to_sql("jobs", conn, if_exists="append", index=False)
    print(f"{len(df)} new records inserted.")
else:
    print("No new records to insert.")

# Step 4: Close connection
conn.commit()
conn.close()

print("Data successfully stored in SQLite database (job_search.db)")


#Run export script after DB update
subprocess.run(["python", "export_to_csv.py"])
print("Export to CSV completed.")