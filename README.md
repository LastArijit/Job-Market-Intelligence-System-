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



## Also Open Source

- **[cv-santiago](https://github.com/santifer/cv-santiago)** -- The portfolio website (santifer.io) with AI chatbot, LLMOps dashboard, and case studies. If you need a portfolio to showcase alongside your job search, fork it and make it yours.

## About the Author

I'm Santiago -- Head of Applied AI, former founder (built and sold a business that still runs with my name on it). I built career-ops to manage my own job search. It worked: I used it to land my current role.

My portfolio and other open source projects → [santifer.io](https://santifer.io)

☕ [Buy me a coffee](https://buymeacoffee.com/santifer) if career-ops helped your job search.

## Star History

<a href="https://www.star-history.com/?repos=santifer%2Fcareer-ops&type=timeline&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=santifer/career-ops&type=timeline&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=santifer/career-ops&type=timeline&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=santifer/career-ops&type=timeline&legend=top-left" />
 </picture>
</a>

## Disclaimer

**career-ops is a local, open-source tool — NOT a hosted service.** By using this software, you acknowledge:

1. **You control your data.** Your CV, contact info, and personal data stay on your machine and are sent directly to the AI provider you choose (Anthropic, OpenAI, etc.). We do not collect, store, or have access to any of your data.
2. **You control the AI.** The default prompts instruct the AI not to auto-submit applications, but AI models can behave unpredictably. If you modify the prompts or use different models, you do so at your own risk. **Always review AI-generated content for accuracy before submitting.**
3. **You comply with third-party ToS.** You must use this tool in accordance with the Terms of Service of the career portals you interact with (Greenhouse, Lever, Workday, LinkedIn, etc.). Do not use this tool to spam employers or overwhelm ATS systems.
4. **No guarantees.** Evaluations are recommendations, not truth. AI models may hallucinate skills or experience. The authors are not liable for employment outcomes, rejected applications, account restrictions, or any other consequences.

See [LEGAL_DISCLAIMER.md](LEGAL_DISCLAIMER.md) for full details. This software is provided under the [MIT License](LICENSE) "as is", without warranty of any kind.

## Contributors

<a href="https://github.com/santifer/career-ops/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=santifer/career-ops" />
</a>

Got hired using career-ops? [Share your story!](https://github.com/santifer/career-ops/issues/new?template=i-got-hired.yml)

## License

MIT

## Let's Connect

[![Website](https://img.shields.io/badge/santifer.io-000?style=for-the-badge&logo=safari&logoColor=white)](https://santifer.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santifer)
[![X](https://img.shields.io/badge/X-000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/santifer)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/8pRpHETxa4)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hi@santifer.io)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/santifer)
