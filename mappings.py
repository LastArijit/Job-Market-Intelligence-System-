ROLE_MAP = {
    # TECH / ENGINEERING
    "site reliability engineer": "Site Reliability Engineer",
    "software development engineer": "Software Engineer",
    "software engineer": "Software Engineer",
    "software developer": "Software Engineer",
    "application developer": "Software Engineer",
    "backend engineer": "Backend Developer",
    "backend developer": "Backend Developer",
    "front end developer": "Frontend Developer",
    "frontend developer": "Frontend Developer",
    "full stack engineer": "Full Stack Developer",
    "full stack developer": "Full Stack Developer",
    "sde": "Software Engineer",
    "swe": "Software Engineer",
    "qa engineer": "QA Engineer",
    "quality assurance engineer": "QA Engineer",
    "test engineer": "QA Engineer",
    "automation engineer": "QA Engineer",
    "devops engineer": "DevOps Engineer",
    "platform engineer": "Platform Engineer",
    "cloud support engineer": "Cloud Support Engineer",
    "cloud engineer": "Cloud Engineer",
    "cloud architect": "Cloud Architect",
    "security engineer": "Cybersecurity Engineer",
    "cyber security": "Cybersecurity Engineer",
    "cybersecurity": "Cybersecurity Engineer",
    "network engineer": "Network Engineer",
    "system engineer": "Systems Engineer",
    "systems engineer": "Systems Engineer",
    "mulesoft developer": "Integration Developer",
    "integration engineer": "Integration Developer",
    "blockchain developer": "Blockchain Developer",
    "embedded engineer": "Embedded Engineer",
    "firmware engineer": "Embedded Engineer",
    "physical design engineer": "VLSI Physical Design Engineer",
    "vlsi": "VLSI Physical Design Engineer",
    "maintenance engineer": "Maintenance Engineer",
    "project engineer": "Project Engineer",
    "architect": "Solutions Architect",

    # AI / DATA
    "machine learning engineer": "Machine Learning Engineer",
    "ai engineer": "AI Engineer",
    "ml engineer": "Machine Learning Engineer",
    "data scientist": "Data Scientist",
    "data engineer": "Data Engineer",
    "data analyst": "Data Analyst",
    "business analyst": "Business Analyst",
    "analytics engineer": "Analytics Engineer",
    "bi developer": "BI Developer",
    "power bi": "BI Developer",
    "tableau": "BI Developer",
    "quantitative analyst": "Quantitative Analyst",
    "quant analyst": "Quantitative Analyst",
    "nlp engineer": "NLP Engineer",
    "nlp": "NLP Engineer",
    "computer vision": "Computer Vision Engineer",
    "ai-powered": "AI Specialist",

    # PRODUCT / DESIGN
    "product manager": "Product Manager",
    "program manager": "Program Manager",
    "project manager": "Project Manager",
    "product owner": "Product Manager",
    "ui/ux designer": "UI UX Designer",
    "ux designer": "UI UX Designer",
    "ui designer": "UI UX Designer",
    "graphic designer": "Graphic Designer",

    # MARKETING / GROWTH / CONTENT
    "digital strategist": "Digital Marketing Strategist",
    "growth manager": "Growth Manager",
    "growth marketer": "Growth Marketing Specialist",
    "performance marketer": "Performance Marketing Specialist",
    "seo specialist": "SEO Specialist",
    "content strategist": "Content Strategist",
    "social engagement specialist": "Social Media Specialist",
    "social media manager": "Social Media Manager",
    "brand manager": "Brand Manager",

    # SALES / BUSINESS DEVELOPMENT
    "sales trainee": "Sales Trainee",
    "sales executive": "Sales Executive",
    "sales manager": "Sales Manager",
    "business development manager": "Business Development Manager",
    "business development executive": "Business Development Executive",
    "account executive": "Account Executive",
    "account manager": "Account Manager",
    "key account manager": "Key Account Manager",
    "key account leader": "Key Account Manager",
    "territory business manager": "Territory Sales Manager",
    "territory manager": "Territory Sales Manager",
    "inside sales": "Inside Sales Representative",
    "sdr": "Sales Development Representative",
    "bdr": "Business Development Representative",

    # OPERATIONS / SUPPLY / ADMIN
    "operations manager": "Operations Manager",
    "business operations": "Business Operations Analyst",
    "operations analyst": "Operations Analyst",
    "merchandising": "Merchandising Specialist",
    "sector specialist": "Sector Specialist",
    "supply chain analyst": "Supply Chain Analyst",
    "procurement specialist": "Procurement Specialist",
    "customer care agent": "Customer Support Representative",
    "support engineer": "Technical Support Engineer",
    "customer support": "Customer Support Representative",

    # HR / TALENT
    "human resources": "HR Specialist",
    "human capital": "HR Specialist",
    "talent acquisition": "Talent Acquisition Specialist",
    "recruiter": "Recruiter",
    "hr manager": "HR Manager",
    "people operations": "People Operations Specialist",

    # FINANCE / RISK
    "investment banker": "Investment Banker",
    "financial analyst": "Financial Analyst",
    "chartered accountant": "Chartered Accountant",
    "accountant": "Accountant",
    "equity research": "Equity Research Analyst",
    "risk analyst": "Risk Analyst",
    "portfolio manager": "Portfolio Manager",
    "hedge fund": "Hedge Fund Analyst",
    "quant trader": "Quantitative Trader",
    "private equity": "Private Equity Analyst",
    "fp&a": "FP&A Analyst",
    "finance manager": "Finance Manager",
    "auditor": "Auditor",

    # LEGAL / COMPLIANCE / POLICY
    "regulatory affairs": "Regulatory Affairs Specialist",
    "privacy operations": "Privacy Operations Analyst",
    "compliance officer": "Compliance Officer",
    "compliance": "Compliance Officer",
    "legal counsel": "Legal Counsel",
    "lawyer": "Corporate Lawyer",
    "legal advisor": "Legal Advisor",
    "legal": "Legal Advisor",

    # HEALTHCARE / LIFE SCIENCES
    "doctor": "General Surgeon",
    "cardio": "Cardiologist",
    "neuro": "Neurologist",
    "dentist": "Dentist",
    "hospital administrator": "Hospital Administrator",
    "clinical research": "Clinical Research Associate",
    "product safety analyst": "Pharmacovigilance Analyst",
    "pharmacovigilance": "Pharmacovigilance Analyst",

    # EDUCATION
    "teacher": "Teacher",
    "faculty": "Faculty",
    "lecturer": "Lecturer",
    "instructional designer": "Instructional Designer",
}

DOMAIN_MAP = {
    # Tech
    "Software Engineer": "Tech",
    "Backend Developer": "Tech",
    "Frontend Developer": "Tech",
    "Full Stack Developer": "Tech",
    "QA Engineer": "Tech",
    "DevOps Engineer": "Tech",
    "Platform Engineer": "Tech",
    "Cloud Support Engineer": "Tech",
    "Cloud Engineer": "Tech",
    "Cloud Architect": "Tech",
    "Site Reliability Engineer": "Tech",
    "Cybersecurity Engineer": "Tech",
    "Network Engineer": "Tech",
    "Systems Engineer": "Tech",
    "Integration Developer": "Tech",
    "Blockchain Developer": "Tech",
    "Embedded Engineer": "Tech",
    "VLSI Physical Design Engineer": "Tech",
    "Maintenance Engineer": "Tech",
    "Project Engineer": "Tech",
    "Solutions Architect": "Tech",

    # Data / AI
    "Machine Learning Engineer": "Data",
    "AI Engineer": "Data",
    "AI Specialist": "Data",
    "Data Scientist": "Data",
    "Data Engineer": "Data",
    "Data Analyst": "Data",
    "Business Analyst": "Data",
    "Analytics Engineer": "Data",
    "BI Developer": "Data",
    "Quantitative Analyst": "Data",
    "NLP Engineer": "Data",
    "Computer Vision Engineer": "Data",

    # Product / Design
    "Product Manager": "Product",
    "Program Manager": "Product",
    "Project Manager": "Product",
    "UI UX Designer": "Design",
    "Graphic Designer": "Design",

    # Marketing
    "Digital Marketing Strategist": "Marketing",
    "Growth Manager": "Marketing",
    "Growth Marketing Specialist": "Marketing",
    "Performance Marketing Specialist": "Marketing",
    "SEO Specialist": "Marketing",
    "Content Strategist": "Marketing",
    "Social Media Specialist": "Marketing",
    "Social Media Manager": "Marketing",
    "Brand Manager": "Marketing",

    # Sales
    "Sales Trainee": "Sales",
    "Sales Executive": "Sales",
    "Sales Manager": "Sales",
    "Business Development Manager": "Sales",
    "Business Development Executive": "Sales",
    "Business Development Representative": "Sales",
    "Sales Development Representative": "Sales",
    "Account Executive": "Sales",
    "Account Manager": "Sales",
    "Key Account Manager": "Sales",
    "Territory Sales Manager": "Sales",
    "Inside Sales Representative": "Sales",

    # Operations / Support / HR
    "Operations Manager": "Operations",
    "Business Operations Analyst": "Operations",
    "Operations Analyst": "Operations",
    "Merchandising Specialist": "Operations",
    "Sector Specialist": "Operations",
    "Supply Chain Analyst": "Operations",
    "Procurement Specialist": "Operations",
    "Technical Support Engineer": "Support",
    "Customer Support Representative": "Support",
    "HR Specialist": "HR",
    "Talent Acquisition Specialist": "HR",
    "Recruiter": "HR",
    "HR Manager": "HR",
    "People Operations Specialist": "HR",

    # Finance
    "Investment Banker": "Finance",
    "Financial Analyst": "Finance",
    "Chartered Accountant": "Finance",
    "Accountant": "Finance",
    "Equity Research Analyst": "Finance",
    "Risk Analyst": "Finance",
    "Portfolio Manager": "Finance",
    "Hedge Fund Analyst": "Finance",
    "Quantitative Trader": "Finance",
    "Private Equity Analyst": "Finance",
    "FP&A Analyst": "Finance",
    "Finance Manager": "Finance",
    "Auditor": "Finance",

    # Legal / Compliance
    "Regulatory Affairs Specialist": "Legal",
    "Privacy Operations Analyst": "Legal",
    "Compliance Officer": "Legal",
    "Corporate Lawyer": "Legal",
    "Legal Counsel": "Legal",
    "Legal Advisor": "Legal",

    # Healthcare / Education
    "Cardiologist": "Healthcare",
    "Neurologist": "Healthcare",
    "Dentist": "Healthcare",
    "General Surgeon": "Healthcare",
    "Hospital Administrator": "Healthcare",
    "Clinical Research Associate": "Healthcare",
    "Pharmacovigilance Analyst": "Healthcare",
    "Teacher": "Education",
    "Faculty": "Education",
    "Lecturer": "Education",
    "Instructional Designer": "Education",
}

LEVEL_MAP = [
    ("Executive", [
        "chief executive officer", "chief financial officer", "chief operating officer",
        "chief technology officer", "chief information officer", "chief marketing officer",
        "chief", "founder", "president"
    ]),
    ("Director", [
        "director", "vice president", "assistant vice president",
        "senior vice president", "head of", "head -", "head –", "head,"
    ]),
    ("Manager", [
        "engineering manager", "product manager", "program manager", "project manager",
        "operations manager", "sales manager", "territory manager", "people manager", "manager"
    ]),
    ("Lead", [
        "team lead", "tech lead", "lead ", "lead-", "lead/"
    ]),
    ("Senior", [
        "senior", "sr.", "sr ", "principal", "staff"
    ]),
    ("Mid-Level", [
        "mid-level", "mid level", "mid ", "intermediate", "ii", "iii", "l2", "l3", "level 2", "level 3"
    ]),
    ("Intern", [
        "intern", "internship", "co-op", "coop"
    ]),
    ("Junior", [
        "junior", "jr.", "jr ", "entry level", "entry-level", "entry",
        "fresher", "graduate", "assistant", "associate", "trainee", "apprentice"
    ]),
]
