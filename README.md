# 🌩️ Cloud ETL Modernization with Apache Airflow & AWS

An end-to-end **ETL pipeline** project using **Apache Airflow** for workflow orchestration and **AWS (Redshift, S3)** for scalable cloud storage and data loading. This project simulates a modern, production-ready data engineering environment that ingests mock API data, transforms it, and loads it into a cloud data warehouse.

---

## 📌 Purpose

This project showcases:

- How to orchestrate real-world ETL workflows using Airflow
- Modular task design with Python operators
- Cloud integration with AWS S3 and Redshift
- Local development inside GitHub Codespaces using Docker and DevContainers

---

## ⚙️ Architecture Overview

```text
         +------------+        +------------------+       +------------------+
         | Mock API   | -----> | Airflow DAG:     | ----> | transform_ads.py |
         | (JSON Ads) |        | fetch_ads_data   |       +------------------+
         +------------+                                     |
                                                             v
                                                      +------------------+
                                                      | load_to_redshift |
                                                      +------------------+
                                                             |
                                                             v
                                                    +--------------------+
                                                    | AWS Redshift Table |
                                                    +--------------------+

🚀 Features
	•	🌀 Modular DAGs: fetch_ads_data, transform_ads_data, load_to_redshift
	•	🐳 Dockerized with Airflow 2.7 for easy reproducibility
	•	🧪 Devcontainer-ready for GitHub Codespaces
	•	📥 Mock API input via local files (mock_data)
	•	🧹 Transformation logic via Python scripts
	•	🔺 Cloud Output to AWS Redshift (simulated/optional)



## 🧰 Tech Stack

This project is powered by modern, cloud-friendly, and modular tools built for scalable data workflows.

| Category                | Tools & Technologies                                                  |
|-------------------------|-----------------------------------------------------------------------|
| **Language**            | Python 3.9                                                            |
| **Orchestration**       | Apache Airflow (v2.7.3)                                               |
| **Environment**         | Docker + DevContainer + GitHub Codespaces                            |
| **ETL Scripting**       | Custom Python scripts (`/scripts`) for ingestion, transformation     |
| **Storage (Mocked)**    | AWS S3 (emulated via local directory), AWS Redshift (via placeholder) |
| **Data Format**         | JSON (mock API), CSV (transformed), Pandas DataFrames                |
| **Scheduler**           | Airflow's built-in scheduler & CLI-triggered DAGs                    |
| **Development**         | VS Code + Remote Containers + GitHub                                |

---

✅ Designed for clarity, portability, and educational purposes.  
📦 Easily extensible to real cloud infrastructure (S3, Redshift, RDS, etc.).


cloud-etl-modernization-airflow-aws/
│
├── .devcontainer/                # DevContainer setup for Codespaces
│   ├── Dockerfile
│   └── devcontainer.json
│
├── dags/                         # Airflow DAGs
│   └── api_ingestion_dag.py
│
├── mock_data/                    # Simulated API data
│   └── ads_data.json
│
├── scripts/                      # ETL scripts
│   ├── transform_ads_data.py
│   └── load_to_redshift.py
│
├── docker-compose.yml           # Airflow service definitions
└── README.md

⚙️ How to Run (Locally or in Codespaces)

✅ Prerequisites
	•	GitHub Codespaces OR Docker & Python 3.9 locally
	•	AWS credentials (if testing with real Redshift)
	•	Replace Redshift config in load_to_redshift.py if connecting to real DB

▶️ Local Setup
# Clone this repo
git clone https://github.com/bashoori/cloud-etl-modernization-airflow-aws
cd cloud-etl-modernization-airflow-aws

# Launch Airflow using Docker Compose
docker-compose up --build

Then visit: http://localhost:8080
	•	Default credentials: admin / admin (or set via Airflow CLI)

🧪 Airflow UI (Live Demo in Codespaces)

The project auto-starts:
	•	Airflow scheduler
	•	Airflow webserver
	•	Database migration
	•	Admin user creation

No setup needed! Just open Port 8080 from your Codespace.

⸻



# 📌 Notable Airflow DAGs

This project includes modular Airflow DAGs designed for modern ETL workflows. Each DAG is focused on a specific stage of the data pipeline, from data ingestion to transformation and loading.

## DAG: `api_ingestion_dag`

An end-to-end DAG that orchestrates the entire pipeline:
1. **Ingests** mock advertisement data (JSON) from a local mock source
2. **Transforms** raw JSON into structured tabular format
3. **Loads** cleaned data into AWS Redshift (or mock DB in development)

### 📂 Tasks Breakdown:

| Task ID            | Description                                | Operator       |
|--------------------|--------------------------------------------|----------------|
| `fetch_ads_data`   | Reads and parses JSON ad data              | PythonOperator |
| `transform_ads`    | Cleans and structures the ads data         | PythonOperator |
| `load_to_redshift` | Writes the transformed data to Redshift    | PythonOperator |

### ⚙️ DAG Config:

- **Schedule**: `@daily`
- **Retries**: `1` (with delay)
- **Owner**: `bita`
- **Dependencies**: `transform_ads` depends on `fetch_ads_data`; `load_to_redshift` runs last.

---

## 💡 DAG Highlights

- Modular and readable — easy to expand for other datasets
- Local JSON ingestion simulates external API
- Transformation and loading logic is abstracted into Python scripts in `/scripts`
- Fully reproducible using Docker and GitHub Codespaces

---

## 🧪 How to Use in Airflow

Once Airflow is running (via Docker or Codespaces), the DAG should appear automatically in the UI.  
Activate it and trigger manually or wait for the daily schedule.

---

> ✨ This DAG is part of the [cloud-etl-modernization-airflow-aws](https://github.com/bashoori/cloud-etl-modernization-airflow-aws) project.



✨ Highlights
	•	Runs on Docker in VS Code + Codespaces
	•	Hands-on Airflow DAG design
	•	Modular structure — easy to plug in APIs, cloud storage, DBs
	•	Great starting point for cloud-native ETL projects

⸻

📈 Future Improvements
	•	Connect to real APIs like Facebook Ads or Google Analytics
	•	Replace SQLite with PostgreSQL for dev DB
	•	Add automated tests and monitoring DAGs
	•	Enable dbt for advanced transformations

⸻

🙋‍♀️ Author

Bita Ashoori
Connect on LinkedIn
GitHub: bashoori

⸻

💡 This project is part of my Data Engineering Portfolio.
