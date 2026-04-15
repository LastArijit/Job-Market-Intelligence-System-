-- SQLite schema for Job Market Analysis
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,
    clean_title TEXT,
    company TEXT,
    location TEXT,
    job_type TEXT,
    work_mode TEXT,
    salary TEXT,
    job_url TEXT UNIQUE NOT NULL,
    posted_date TEXT,
    level TEXT,
    domain TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Jobs by Location (Demand)
CREATE VIEW vw_jobs_by_location AS
SELECT
    COALESCE(location, 'Unknown') AS location,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY location;

-- Jobs by Role (Clean Title)
CREATE VIEW vw_jobs_by_role AS
SELECT
    clean_title,
    COUNT(*) AS total_jobs
FROM jobs
WHERE domain != 'General'
GROUP BY clean_title;

-- Hiring Companies
CREATE VIEW vw_top_companies AS
SELECT
    COALESCE(company, 'Unknown') AS company,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY company;

-- Jobs by Level
CREATE VIEW vw_jobs_by_level AS
SELECT
    COALESCE(level, 'Unknown') AS level,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY level;

-- Jobs by Domain
CREATE VIEW vw_jobs_by_domain AS
SELECT
    COALESCE(domain, 'Unknown') AS domain,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY domain;

-- Work Mode Distribution
CREATE VIEW vw_work_mode_distribution AS
SELECT
    COALESCE(work_mode, 'Unknown') AS work_mode,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY work_mode;

-- Jobs Over Time
CREATE VIEW vw_jobs_over_time AS
SELECT
    DATE(posted_date) AS job_date,
    COUNT(*) AS total_jobs
FROM jobs
WHERE posted_date IS NOT NULL
GROUP BY DATE(posted_date);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_jobs_location ON jobs(location);
CREATE INDEX IF NOT EXISTS idx_jobs_clean_title ON jobs(clean_title);