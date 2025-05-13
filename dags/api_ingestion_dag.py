#Purpose: Orchestrates daily data ingestion from API to AWS S3.

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests, json, boto3

def fetch_ads_data():
    url = "https://api.mockadsplatform.com/data"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            s3 = boto3.client('s3')
            s3.put_object(Bucket='your-bucket-name', Key='raw/ads_data.json', Body=json.dumps(data))
        else:
            raise Exception(f"Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

default_args = {
    'owner': 'bita',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('api_ingestion_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    task_fetch = PythonOperator(
        task_id='fetch_ads_data',
        python_callable=fetch_ads_data
    )

    task_fetch