# IMPORTING LIBRARIES

import requests
import pandas as pd
import sqlite3

# requests → used to call the API (fetch data from internet)
# pandas → used to organize data into a table and save as CSV
# Sqlite3 → used to connect to a SQL database

#-----------------------------------------------------------------------------------
# API DATA EXTRACTION

# url part
url = "https://jsearch.p.rapidapi.com/search"
# Broad query to fetch mixed jobs
query = "jobs"

#params part
querystring = {
    "query": query,
    "page": "1",
    "num_pages": "30"   # ~100 jobs (approx) after verifying duplicates
}

#headers part
headers = {
    "X-RapidAPI-Key": "da1697a4a9msh058f938cfd3ee4cp13548ajsned43763a0645",
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers = headers, params = querystring)

# Convert response into Python dict - json format
data = response.json()

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

# Limit to ~100 jobs
df = df.head(100)

#-------------------------------------------------------------------------------------------
# DATA CLEANING

#Remove duplicates in job_url
df = df.drop_duplicates(subset=['job_url'])


#Drop rows where critical fields are missing
df = df.dropna(subset=['title', 'job_url'])
# Fill non-critical missing values
df['company'] = df['company'].fillna("Unknown")
df['location'] = df['location'].fillna("Not Specified")
df['salary'] = df['salary'].fillna("Not Disclosed")
df['posted_date'] = df['posted_date'].fillna("Not Available")

#Standardizing title, company, location
df['title'] = df['title'].str.strip().str.title()
df['company'] = df['company'].str.strip().str.title()
df['location'] = df['location'].str.strip().str.title()

def clean_location(loc):
    loc = str(loc).lower()

    if "remote" in loc:
        return "Remote"
    elif loc in ["not specified", "none"]:
        return "Not Specified"
    else:
        return loc.title()

df['location'] = df['location'].apply(clean_location)

#Adding level and domain columns in the dataframe based on the title
def extract_features(title):
    title = str(title).lower()

    # Level Detection(senior, Junior, Mid-Level)

    if any(word in title for word in [
        "senior", "sr.", "lead", "principal",
        "head", "director", "manager", "vp",
        "consultant", "expert"
    ]):
        level = "Senior"

    elif any(word in title for word in [
        "junior", "jr.", "associate", "entry",
        "trainee", "intern", "fresher",
        "graduate", "apprentice", "assistant"
    ]):
        level = "Junior"

    elif any(word in title for word in [
        "mid", "intermediate", "ii", "iii",
        "level 2", "level 3"
    ]):
        level = "Mid-Level"

    else:
        level = "Not Specified"


    # Domain Detection(Marketing, Business Intelligence, Data Science & AI, Data Engineering,
    # Finance, Product, Sales, Operations, HR & People, Healthcare, Digital Analytics, if none then General.

    if any(word in title for word in [
        "marketing", "seo", "sem", "campaign",
        "brand", "content", "growth"
    ]):
        domain = "Marketing"

    elif any(word in title for word in [
        "business intelligence", "bi", "dashboard",
        "reporting", "tableau", "power bi"
    ]):
        domain = "Business Intelligence"

    elif any(word in title for word in [
        "machine learning", "ai", "data science",
        "nlp", "deep learning"
    ]):
        domain = "Data Science & AI"

    elif any(word in title for word in [
        "data engineer", "pipeline", "spark",
        "hadoop", "etl", "cloud"
    ]):
        domain = "Data Engineering"

    elif any(word in title for word in [
        "finance", "risk", "banking", "audit"
    ]):
        domain = "Finance"

    elif any(word in title for word in [
        "product", "ux", "a/b test"
    ]):
        domain = "Product"

    elif any(word in title for word in [
        "sales", "crm", "revenue"
    ]):
        domain = "Sales"

    elif any(word in title for word in [
        "operations", "logistics", "supply chain"
    ]):
        domain = "Operations"

    elif any(word in title for word in [
        "hr", "recruitment", "talent"
    ]):
        domain = "HR & People"

    elif any(word in title for word in [
        "healthcare", "clinical", "medical"
    ]):
        domain = "Healthcare"

    elif any(word in title for word in [
        "digital", "web", "ecommerce"
    ]):
        domain = "Digital Analytics"

    else:
        domain = "General"

    return pd.Series([level, domain])

# Add the columns and apply the conditions
df[['level', 'domain']] = df['title'].apply(extract_features)

# Save to CSV
df.to_csv("jobs.csv", index=False)
print('Data successfully saved to jobs.csv')

#------------------------------------------------------------------------------------------------
# SQLITE DATABASE SETUP + Add data from dataframe to job.db

#Create Database jobs.db
conn = sqlite3.connect("jobs.db")
#Create cursor object
cursor = conn.cursor()

# Create table (Re-running precaution set)
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    job_type TEXT,
    salary TEXT,
    job_url TEXT UNIQUE,
    posted_date TEXT,
    work_mode TEXT,
    level TEXT,
    domain TEXT
)
""")
conn.commit()

# Duplicate Jobs Removal
cursor.execute("SELECT job_url FROM jobs")
existing_urls = set([row[0] for row in cursor.fetchall()])
df = df[~df['job_url'].isin(existing_urls)]

#Saving DataFrame to the Database
df.to_sql("jobs", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("Data successfully stored in SQLite database (jobs.db)")

