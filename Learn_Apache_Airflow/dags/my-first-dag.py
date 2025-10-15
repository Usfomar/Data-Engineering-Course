from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

# Define file paths


input_file = "/etc/passwd"
extracted_file = "/opt/airflow/data/extracted-data.txt"
transformed_file = "/opt/airflow/data/transformed_data.csv"
output_file = "/opt/airflow/data/output-data-analytics.csv"

# Extraction
def extract():
    print("Extraction Phase")
    with open(input_file, "r") as infile, open(extracted_file, "w") as outfile:
        for line in infile:
            ls = line.split(":")
            s = ls[0] + ":" + ls[2] + ":" + ls[5] + "\n"
            outfile.write(s)

# Transformation
def transform():
    print("Transformation Phase")
    with open(extracted_file, "r") as infile, open(transformed_file, "w") as outfile:
        for line in infile:
            s = line.replace(":", ",")
            outfile.write(s)

# Load
def load():
    print("Loading Phase")
    with open(transformed_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            outfile.write(line)

# Check
def check():
    print("Check Phase")
    with open(output_file, "r") as f:
        for line in f:
            print(line)

default_args = {
    "owner": "usfomar",
    "start_date": datetime(2025, 10, 4),
    "email": "yousefomar720@gmail.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag= DAG(
    dag_id="my_first_python_etl_dag",
    default_args=default_args,
    description="My first ETL DAG",
    schedule=timedelta(days=1),
    catchup=False,
) 

execute_extract = PythonOperator(
    task_id="extract",
    python_callable=extract,
    dag=dag
)

execute_transform = PythonOperator(
    task_id="transform",
    python_callable=transform,
    dag=dag
)

execute_load = PythonOperator(
    task_id="load",
    python_callable=load,
    dag=dag
)

execute_check = PythonOperator(
    task_id="check",
    python_callable=check,
    dag=dag
)

# Task Pipeline
execute_extract >> execute_transform >> execute_load >> execute_check