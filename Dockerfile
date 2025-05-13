# Dockerfile
#Dockerfile (for Airflow + Python environment)

FROM apache/airflow:2.7.3-python3.10

USER root

# Install additional Python packages
RUN pip install --no-cache-dir pandas boto3 requests

USER airflow