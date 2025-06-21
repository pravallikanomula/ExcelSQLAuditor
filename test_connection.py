import pyodbc
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Build connection string
conn_str = (
    f"DRIVER={os.getenv('DB_DRIVER')};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_DATABASE')};"
    f"UID={os.getenv('DB_USER')};"
    f"PWD={os.getenv('DB_PASSWORD')}"
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.databases")
    print("✅ Connected! Databases on server:")
    for row in cursor.fetchall():
        print("-", row.name)
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
