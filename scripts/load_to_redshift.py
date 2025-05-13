"""
Purpose: Load transformed ad data from CSV (processed_data.csv)
         into an AWS Redshift table using psycopg2.
"""

import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# -----------------------------
# 🔐 AWS / Redshift Config from .env
# -----------------------------
REDSHIFT_HOST = os.getenv("REDSHIFT_HOST")
REDSHIFT_DB = os.getenv("REDSHIFT_DB")
REDSHIFT_USER = os.getenv("REDSHIFT_USER")
REDSHIFT_PASSWORD = os.getenv("REDSHIFT_PASSWORD")
REDSHIFT_PORT = os.getenv("REDSHIFT_PORT", 5439)

CSV_FILE_PATH = "mock_data/processed_data.csv"
TABLE_NAME = "ads_metrics"  # Replace with your Redshift table name

def load_to_redshift():
    try:
        # Read CSV
        df = pd.read_csv(CSV_FILE_PATH)

        # Connect to Redshift
        conn = psycopg2.connect(
            host=REDSHIFT_HOST,
            dbname=REDSHIFT_DB,
            user=REDSHIFT_USER,
            password=REDSHIFT_PASSWORD,
            port=REDSHIFT_PORT
        )
        cur = conn.cursor()

        # Optional: Create table if not exists (basic schema)
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            ad_id VARCHAR(50),
            impressions INT,
            clicks INT,
            spend FLOAT,
            ctr FLOAT,
            cpc FLOAT
        );
        """
        cur.execute(create_table_sql)

        # Insert data row-by-row
        for _, row in df.iterrows():
            cur.execute(
                f"""
                INSERT INTO {TABLE_NAME} (ad_id, impressions, clicks, spend, ctr, cpc)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (row.ad_id, row.impressions, row.clicks, row.spend, row.ctr, row.cpc)
            )

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Data successfully loaded into Redshift!")

    except Exception as e:
        print(f"❌ Error loading data to Redshift: {e}")

if __name__ == "__main__":
    load_to_redshift()