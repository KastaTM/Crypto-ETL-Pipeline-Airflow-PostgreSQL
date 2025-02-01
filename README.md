# 🚀 Crypto ETL Pipeline with Apache Airflow & PostgreSQL

## 📌 Overview
This project is a **Data Engineering Pipeline** that extracts real-time cryptocurrency data from the **CoinGecko API**, transforms it, and loads it into a **PostgreSQL database** using **Apache Airflow** for automation.

## 📂 Project Structure
```
📁 project_root/
│-- 📁 airflow/          # Apache Airflow environment
│   │-- 📁 dags/         # DAGs directory for Airflow
│   │   ├── etl_pipeline.py   # DAG definition
│-- 📁 scripts/         # Python scripts for ETL process
│   │-- etl_pipeline.py  # Extract, Transform, Load process
│-- README.md           # Project documentation
```

## ⚙️ Technologies Used
- **Python** 🐍
- **Apache Airflow** ⏳
- **PostgreSQL** 🗄️
- **SQLAlchemy** 🔗
- **Pandas** 📊
- **CoinGecko API** 🔥

## 🔧 Setup & Installation

### **1️⃣ Install Dependencies**


### **1️⃣ Setup PostgreSQL Database**
```sql
CREATE DATABASE mi_basedatos;
CREATE USER usuario WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE mi_basedatos TO usuario;
```

### **2️⃣ Configure Airflow**
```bash
export AIRFLOW_HOME=~/airflow
airflow db init
airflow users create --username admin --password admin --firstname John --lastname Doe --role Admin --email admin@example.com
```

### **3️ Move DAG to Airflow Directory**
```bash
mv etl_pipeline.py ~/airflow/dags/
```

### **4️⃣ Start Airflow**
```bash
airflow scheduler &
airflow webserver -p 8080 &
```
Access Airflow UI at 👉 [http://localhost:8080](http://localhost:8080)

## 🔄 Running the ETL Pipeline
### **Manually Trigger DAG in Airflow UI**
1. Log into Airflow UI
2. Find `crypto_etl`
3. Toggle **ON** and click **Trigger DAG** ▶️

### **Verify Data in PostgreSQL**
```bash
sudo -u postgres psql
```
```sql
\c mi_basedatos;
SELECT * FROM public.crypto_data LIMIT 10;
```

## 📌 Future Enhancements
✅ Add Data Visualization with **Tableau/Power BI** 📊
✅ Implement **Docker** for better deployment 🐳
✅ Use **Apache Kafka** for real-time data streaming 🔄

