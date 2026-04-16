# Job-Market-Intelligence-System

<p align="left">
  <img width="700" src="https://github.com/user-attachments/assets/d3068878-c07a-4ccb-80d4-e444582e0abb" />
</p>

<p align="left">
  <em>Having just graduated, I wanted a clearer view of the job market.</em><br>
But the reality was different.<br>
Messy data. Duplicate roles. No signal — just noise.<br><br>

Tracking it manually was inefficient. So I stopped searching for a solution — and built one.<br><br>

<strong>A pipeline that collects, cleans, and structures job data into something actually usable.</strong><br>
<em>Something you can analyze. Something that reveals patterns.</em><br><br>

What started as a personal fix became something bigger.<br>
<em>So I open sourced it — because this problem isn’t just mine.</em>
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Curser-000?style=flat&logo=anthropic&logoColor=white" alt="Curser">
  <img src="https://img.shields.io/badge/PowerBI-111827?style=flat&logo=terminal&logoColor=white" alt="PowerBI">
  <img src="https://img.shields.io/badge/Codex_(soon)-6B7280?style=flat&logo=openai&logoColor=white" alt="Codex">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/API-JSearch-blue?style=flat" alt="API">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT">
</p>

---

# Project Overview
The job market generates an overwhelming amount of data every day, yet most of it is unstructured, duplicated, and difficult to analyze.

This project builds a structured pipeline capable of:

- Collecting job listings from external APIs  
- Cleaning and standardizing inconsistent data  
- Removing duplicates and noise  
- Classifying roles into meaningful domains  
- Storing structured data for analysis  
- Enabling queries to uncover hiring trends and patterns  

The goal is to transform scattered job listings into a clean, scalable dataset that can be used for meaningful analysis and decision-making.

> **Note:** This README serves as an introduction to the project — explaining the pipeline, how it works, and the thinking behind it.  
>  
> The project is also documented in three phases, reflecting how it was built in real time. Each phase captures the challenges encountered, the points where things broke down, and how those problems were solved.  
>  
> This process is a core part of data engineering — understanding where systems fail, and learning how to connect the dots to make them work reliably.

---

## 📂 Project Structure

The project is organized into modular scripts, each responsible for a specific stage of the pipeline:

| File | Description |
|------|------------|
| `Job_list.py` | Main pipeline script that orchestrates the workflow — fetches data, cleans it, applies transformations, and stores results in the database. |
| `mappings.py` | Contains rule-based mappings for standardizing job titles, assigning domains, and detecting seniority levels. |
| `ai_implementation.py` | Uses AI to classify and clean job roles that could not be categorized using rule-based logic. |
| `create_database.py` | Initializes the SQLite database by executing the schema and creating tables, indexes, and views. |
| `schema.sql` | Defines the database structure, including tables and relationships. |
| `export_to_csv.py` | Extracts structured data from the database and exports it into a CSV file. |
| `jobs_data.csv` | Final processed dataset containing cleaned job listings. |
| `job_search.db` | SQLite database storing all processed job data. |
| `Job_Market_Analysis_Dashboard.pbix` | Power BI dashboard used for visualizing job market insights. |

---
## How It Works

```
Fetch Job Data (JSearch API)
│
▼
┌──────────────────────────┐
│ Raw Data Extraction │ Extracts key fields from nested JSON
│ │ (title, company, location, URL, etc.)
└──────────┬───────────────┘
│
▼
┌──────────────────────────┐
│ Data Cleaning │ Handles missing values, normalizes text,
│ │ removes URL tracking noise
└──────────┬───────────────┘
│
▼
┌──────────────────────────┐
│ Rule-Based Mapping │ Uses ROLE_MAP, DOMAIN_MAP, LEVEL_MAP
│ │ to standardize titles and classify roles
└──────────┬───────────────┘
│
▼
┌──────────────────────────┐
│ AI Enhancement Layer │ Processes "General" roles using Gemini
│ │ for refined classification
└──────────┬───────────────┘
│
▼
┌──────────────────────────┐
│ Deduplication Engine │ Removes duplicates using job URLs
│ │ (DB + in-memory checks)
└──────────┬───────────────┘
│
▼
┌──────────────────────────┐
│ SQLite Storage │ Stores structured data for querying
│ │ and persistence
└──────────┬───────────────┘
│
▼
┌──────┼────────┐
▼ ▼ ▼
CSV Database Dashboard
Export (.db) (Power BI)
```

### 🔍 Key Components

- **JSearch API** → Source of raw job listings  
- **Pandas** → Data cleaning and transformation  
- **Rule-Based Mapping** → Standardizes titles, domains, and levels  
- **Gemini API** → Handles edge cases and improves classification  
- **SQLite** → Stores structured data for querying  
- **Power BI** → Visualizes insights and trends 

---
## ❓ Questions This Project Answers

Once the data is structured and stored, the pipeline enables analysis of key job market trends, such as:

- **Which job roles are most in demand?**  
  Identify the most frequently occurring job titles across the dataset.

- **Which domains are hiring the most?**  
  Compare demand across domains like Tech, Data, Finance, Marketing, etc.

- **What is the distribution of experience levels?**  
  Understand how many roles are Junior, Mid-level, or Senior.

- **Which companies are hiring most actively?**  
  Identify companies with the highest number of job postings.

- **What are the most common job locations?**  
  Analyze geographic distribution of job opportunities.

- **What proportion of jobs are Remote vs On-site vs Hybrid?**  
  Understand work mode trends in the job market.

- **How frequently are new jobs being posted?**  
  Track job posting activity over time.

- **Are there patterns in job titles and domains?**  
  Discover relationships between roles, levels, and domains.

- **How much noise exists in raw job data?**  
  Compare raw vs cleaned data to understand the impact of preprocessing.

---
## ⚠️ Limitations

While the pipeline provides a structured and scalable approach to job market analysis, it has a few limitations:

- **Limited Data Source Coverage**  
  The project currently relies on the JSearch API, which may not capture the full job market and can introduce source bias.

- **API Rate Limits & Quotas**  
  Data collection is constrained by API limits, which can restrict the volume and frequency of data updates.

- **Heuristic-Based Classification**  
  Rule-based mappings (ROLE_MAP, DOMAIN_MAP, LEVEL_MAP) may not fully capture the complexity of real-world job titles.

- **AI Dependency for Edge Cases**  
  The AI layer improves classification but depends on external APIs, which may introduce latency, cost, or occasional inconsistencies.

- **Data Freshness**  
  The dataset reflects snapshots of job listings rather than a continuous real-time stream.

- **Geographic Scope**  
  Data collection is currently focused on India-based roles, which may limit global generalization.

- **Simplified Data Model**  
  The database schema is intentionally lightweight and may not capture deeper relationships (e.g., skills, salary normalization, company metadata).

- **Potential Data Noise**  
  Despite cleaning, some inconsistencies or misclassifications may still persist in real-world data.

---
## 🎥 Video Overview

A complete walkthrough of the project, covering the pipeline, architecture, and key components:

👉 [Watch the video overview](#)

In this video, I walk through:

- How the data pipeline is structured  
- How job data is collected, cleaned, and stored  
- The role of rule-based mappings and AI in classification  
- Database design and deduplication logic  
- How the final dataset is used for analysis and visualization  

This provides a clear end-to-end understanding of how the system works in practice.
