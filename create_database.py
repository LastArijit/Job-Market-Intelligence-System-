
import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("job_search.db")
cursor = conn.cursor()

# Read schema.sql file
with open("schema.sql", "r") as f:
    sql_script = f.read()

# Execute all SQL commands (tables, views, indexes, etc.)
cursor.executescript(sql_script)

# Save changes and close
conn.commit()
conn.close()

print("Database, tables, views, and indexes created successfully.")