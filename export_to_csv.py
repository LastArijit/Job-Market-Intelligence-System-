import sqlite3
import pandas as pd

#Connect to database
conn = sqlite3.connect("job_search.db")
query = "SELECT * FROM jobs"
df = pd.read_sql_query(query, conn)
conn.close()
# Export to CSV
df.to_csv("jobs_data.csv", index=False)

print("CSV file created successfully: jobs_data.csv")