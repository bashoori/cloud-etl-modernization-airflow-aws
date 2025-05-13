# 🌩️ Cloud ETL Modernization with Apache Airflow & AWS

An end-to-end **ETL pipeline** project using **Apache Airflow** for workflow orchestration and **AWS (Redshift, S3)** for scalable cloud storage and data loading.  
It simulates a modern, production-ready data engineering environment for ingesting mock API data, transforming it, and loading it into a cloud data warehouse.

---

## 📌 Purpose

- Demonstrate orchestrated ETL pipelines using Airflow
- Modular task design with Python
- Cloud integration with AWS S3 & Redshift (mocked)
- DevContainer + Codespaces for portable, reproducible dev

---

## ⚙️ Architecture Overview

```text
+------------+       +---------------------+       +---------------------+
|  Mock API  | --->  |  fetch_ads_data     | --->  |  transform_ads.py   |
| (JSON Ads) |       |  (Airflow DAG Task) |       | (Transforms to CSV) |
+------------+       +---------------------+       +---------------------+
                                                 |
                                                 v
                                       +-------------------------+
                                       |  load_to_redshift.py    |
                                       | (Load to Redshift Table)|
                                       +-------------------------+
                                                 |
                                                 v
                                       +-------------------------+
                                       |   AWS Redshift Table    |
                                       +-------------------------+

## 🚀 Features

- 🌀 Modular DAGs: `fetch_ads_data`, `transform_ads`, `load_to_redshift`
- 🐳 Dockerized with Airflow 2.7 for easy reproducibility
- 🧪 Devcontainer-ready for GitHub Codespaces
- 📥 Mock API input via local files (`mock_data`)
- 🔄 Python-based transformations
- 🔺 Simulated Redshift loading

---

## 🧰 Tech Stack

| Category              | Tools & Technologies                                                  |
|-----------------------|-----------------------------------------------------------------------|
| **Language**          | Python 3.9                                                            |
| **Orchestration**     | Apache Airflow (v2.7.3)                                               |
| **Environment**       | Docker, DevContainers, GitHub Codespaces                             |
| **ETL Scripting**     | Python scripts (`/scripts`)                                           |
| **Storage (Mocked)**  | AWS S3 (local dir), AWS Redshift (simulated)                         |
| **Data Format**       | JSON input, CSV output, Pandas DataFrames                            |
| **Dev Tooling**       | VS Code + Remote Containers                                           |

✅ Built for clarity and learning  
📦 Ready to adapt to real infrastructure (S3, RDS, Redshift, etc.)

---

## 📁 Project Structure
cloud-etl-modernization-airflow-aws/
│
├── .devcontainer/                # Devcontainer setup
│   ├── Dockerfile
│   └── devcontainer.json
│
├── dags/                         # Airflow DAGs
│   └── api_ingestion_dag.py
│
├── mock_data/                    # Mock JSON input
│   └── ads_data.json
│
├── scripts/                      # ETL logic
│   ├── transform_ads_data.py
│   └── load_to_redshift.py
│
├── docker-compose.yml           # Airflow stack
└── README.md

---

## ▶️ How to Run

### ✅ Prerequisites

- GitHub Codespaces **or** local Docker
- Python 3.9+
- AWS Redshift creds (optional)

### 🚀 Local Setup

```bash
git clone https://github.com/bashoori/cloud-etl-modernization-airflow-aws
cd cloud-etl-modernization-airflow-aws
docker-compose up --build

Then visit: http://localhost:8080
→ Default login: admin / admin

⸻

🧪 Codespaces Experience
	•	Starts the Airflow scheduler & webserver automatically
	•	Database migration & admin user setup is handled in postCreateCommand
	•	Open port 8080 to access the UI instantly

⸻

📌 Notable Airflow DAGs

### `api_ingestion_dag.py`

Orchestrates the ETL flow:

| **Task ID**         | **Description**                         | **Operator**     |
|---------------------|-----------------------------------------|------------------|
| `fetch_ads_data`    | Reads JSON ad data                      | PythonOperator   |
| `transform_ads`     | Cleans/structures data                  | PythonOperator   |
| `load_to_redshift`  | Loads to Redshift or mock destination   | PythonOperator   |

- ⏰ **Schedule**: `@daily`  
- 🔁 **Retries**: `1`  
- 👤 **Owner**: `bita`



💡 Highlights
	•	Modular, reusable DAG components
	•	Easy to extend with real cloud infra (APIs, Redshift)
	•	Run locally or in the cloud instantly via Codespaces
	•	Clear separation of ingestion, transform, load steps

⸻

📈 Future Improvements
	•	Use real external APIs (Facebook Ads, GA4)
	•	Swap SQLite for PostgreSQL in dev
	•	Add testing suite for DAGs and scripts
	•	Add dbt-based transformations

⸻

🙋‍♀️ Author

Bita Ashoori
GitHub ・ LinkedIn

💼 Part of my Data Engineering Portfolio
