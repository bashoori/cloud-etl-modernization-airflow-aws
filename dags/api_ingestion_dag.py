"""
DAG: api_ingestion_dag
Purpose: Fetch mock ad data from an API and upload it to AWS S3 (securely).
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import json
import os
import boto3
from dotenv import load_dotenv

# Load .env only for local development
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

def fetch_ads_data():
    url = "https://api.mockadsplatform.com/data"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # AWS credentials should be set via environment variables or IAM roles (not hardcoded!)
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )

        bucket_name = os.getenv('AWS_S3_BUCKET')
        s3.put_object(
            Bucket=bucket_name,
            Key='raw/ads_data.json',
            Body=json.dumps(data)
        )

        print(f"✅ Data uploaded to S3 bucket: {bucket_name}/raw/ads_data.json")

    except Exception as e:
        print(f"❌ Failed to fetch or upload ads data: {e}")

default_args = {
    'owner': 'bita',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='api_ingestion_dag',
    default_args=default_args,
    schedule='@daily',  # use `schedule` instead of deprecated `schedule_interval`
    catchup=False,
    tags=['ads', 's3', 'api', 'boto3']
) as dag:

    task_fetch = PythonOperator(
        task_id='fetch_ads_data',
        python_callable=fetch_ads_data
    )