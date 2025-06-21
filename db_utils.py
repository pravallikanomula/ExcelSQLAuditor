import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_sql_data(table_name):
    conn_str = (
        f"DRIVER={os.getenv('DB_DRIVER')};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_DATABASE')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        f"Encrypt=no;"
        f"TrustServerCertificate=yes;"
    )
    print("[INFO] Connecting with:", conn_str.replace(os.getenv("DB_PASSWORD"), "***"))
    
    conn = pyodbc.connect(conn_str)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df
