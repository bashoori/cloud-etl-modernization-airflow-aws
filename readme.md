# Project: cloud-etl-modernization-airflow-aws

## 🚀 Overview
This project modernizes a legacy ETL pipeline using **Apache Airflow**, **AWS**, and **Python**. It demonstrates how to automate data ingestion from third-party APIs, transform the data, and store it in a cloud-native architecture (S3, Redshift). Inspired by a real-world pipeline refactor that reduced processing time by 40% and enabled real-time reporting across business teams.

---

## 🧱 Architecture
**Source**: Mock Ads API / JSON files  
**Orchestration**: Apache Airflow  
**Storage**: AWS S3 (raw layer), optionally Redshift (modeled layer)  
**Transformation**: PySpark / Pandas  
**Deployment**: GitHub Codespaces, Docker, CI/CD with GitHub Actions

---

## 📂 Directory Structure
```
cloud-etl-modernization-airflow-aws/
├── dags/
│   ├── api_ingestion_dag.py          # DAG to ingest ads data into S3
│   ├── data_cleanup_dag.py           # (to be implemented)
│   └── model_refresh_dag.py          # (to be implemented)
├── lambda/
│   └── check_file_trigger.py         # (future: file-based Lambda trigger)
├── scripts/
│   ├── transform_ads_data.py         # Transforms raw ads data into KPIs
│   └── load_to_redshift.py           # (future: Redshift load script)
├── mock_data/
│   └── ads_sample.json               # Sample mock input for local dev
├── configs/
│   └── connections.json              # Airflow connection templates (local)
├── docker-compose.yml                # Local Airflow dev environment
├── .github/workflows/ci-pipeline.yml# CI/CD pipeline via GitHub Actions
├── README.md                         # You’re here
```

---

## ⚙️ Features
- ✅ Modular Airflow DAGs for ingestion, transformation, and loading
- ✅ Serverless ingestion with AWS Lambda & S3
- ✅ Automated transformation using Pandas
- ✅ Configurable to run locally or in the cloud
- ✅ Version-controlled in GitHub Codespaces with CI/CD support

---

## 🧪 How to Run Locally
```bash
# Step 1: Clone the repo
$ git clone https://github.com/yourusername/cloud-etl-modernization-airflow-aws

# Step 2: Launch Airflow locally (requires Docker)
$ docker-compose up -d

# Step 3: Trigger the DAG manually from the Airflow UI
# (http://localhost:8080)
```

---

## 📊 Example Output
Sample output from `transform_ads_data.py`:
```csv
campaign_id,impressions,clicks,spend,date,ctr
abc123,10000,345,123.45,2024-06-01,0.0345
```

---

## 👤 Author
**Bita Ashoori**  
GitHub: [bashoori](https://github.com/bashoori)  

---

## 📜 License
MIT License. Feel free to fork, improve, and contribute!
