from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "crypto_etl",
    default_args=default_args,
    description="ETL Pipeline Airflow cryptocurrency",
    schedule_interval=timedelta(hours=1),
)

def run_etl():
    subprocess.run(["/usr/bin/python3", "/home/student/Desktop/project/etl_pipeline.py"])

etl_task = PythonOperator(
    task_id="run_etl",
    python_callable=run_etl,
    dag=dag,
)

etl_task
