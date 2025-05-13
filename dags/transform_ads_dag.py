# Purpose: Transforms raw ads JSON data into structured CSV format

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json
import pandas as pd
import os

def transform_ads_data():
    raw_path = "/workspaces/cloud-etl-modernization-airflow-aws/mock_data/ads_data.json"
    output_path = "/workspaces/cloud-etl-modernization-airflow-aws/processed_data/ads_data_transformed.csv"

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        with open(raw_path, 'r') as f:
            ads = json.load(f)

        # Flatten JSON to tabular structure
        df = pd.json_normalize(ads)

        # Save as CSV
        df.to_csv(output_path, index=False)
        print(f"✅ Transformed data saved to {output_path}")

    except Exception as e:
        print(f"❌ Error in transformation: {e}")

default_args = {
    'owner': 'bita',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('transform_ads_dag',
         default_args=default_args,
         schedule_interval=None,
         catchup=False) as dag:

    task_transform = PythonOperator(
        task_id='transform_ads_data',
        python_callable=transform_ads_data
    )