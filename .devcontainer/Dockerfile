# Use the official Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /opt/airflow

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    git \
    && apt-get clean

# Upgrade pip
RUN pip install --upgrade pip

# Install Airflow with extras
RUN pip install apache-airflow[postgres,amazon]==2.7.3

# Install project dependencies from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt || true

# Expose Airflow webserver port
EXPOSE 8080

# Set environment variables to avoid Airflow init issues
ENV AIRFLOW_HOME=/opt/airflow