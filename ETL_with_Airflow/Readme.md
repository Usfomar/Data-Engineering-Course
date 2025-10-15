# Learn Apache Airflow


> [!NOTE]
> The process of installing Apache Airflow was quite complex, so I realized that the best way to install and use tools that require many dependencies and environment variable changes is to run them in Docker containers or with Docker Compose.  
> Therefore, I decided to learn Docker—its architecture, the concepts behind it—and it really helped me. It was much more comfortable than installing Airflow directly on the local machine.  
> This project is implemented using Apache Airflow in Docker Compose (since Airflow runs multiple services, Docker Compose is the right way to install and manage it).

> [!NOTE]
> This directory contains all DAGs i implement for learning Apache Airflow, But what i detailed is the final project and all other practices are here too.
> All you should make is to download directory and build and start docker compose `docker compose up` then open Airflow UI and trigger dags.




### Introduction

This simple project is an evidence that i learned and implemented (not deeply) the concepts and tools in this course. I used tools such as :
- Apache Airflow.
- Bash Scripts.
- Python
- The concept of data pipelines.
- Monitoring the ETL process through Apache Airflow UI and CLI.

### Objectvies

**Create a data pipeline that does the following:**
(The project has 2 version one using Bash Operator and the second is implemented using Python Operator)
1. Download data.
2. Extract data with its different data types.
3. Combine the files from different sources and unify its data types to one file.
4. Transform it to conform the requirements.
5. Load transformed data to be used in the future.
6. Schedule the whole process.

### Implementation

Tasks in the pipeline are implemented using bash commands it's easir for me and it's the most straight forward way to perform what it needed. I create a DAG (a python script) using apache airflow to create the pipeline and schedule it.
