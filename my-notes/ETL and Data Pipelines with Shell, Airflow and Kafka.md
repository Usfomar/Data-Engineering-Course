
>[!NOTE]
>I tried to install and run Apache Airflow locally but i faced a lot of problems and it was so complex even though i run it  and open airflow web-server but there are was problems in versioning or compatibility so i decided to learn `Docker contaienrs and Docker compose` and i used it to run and work with Apache Airflow. So i am proud of myself in doing that now i know docker :)






**ETL stands for Extract, Transform and Load**
- **Extract** raw data from multiple sources such as web pages, IoT devices, social media feeds or many other sources.
- **Transform** is the process  that convert the raw data into information can be used and it may contain the following tasks:
	- **Data Cleaning**: handle missing values and fix errors
	- **Filtering**: Select only needed data and discard the rest of it
	- **Joining**: merge data  from multiple tables or sources into single one
	- **Aggregation**: apply some aggregation functions to add more meanings to data
	- **Sorting**
	- **Feature engineering:** means you create new features from existing ones such as creating KPIs for dashboards or machine learning.
	- **Encrypting**
	- **Normalizing:** establish common units 
	- **Data Structuring**: change the data types or the structure of data to the most needed ones
- **Load** is the process of storing transformed data into a new environment that ensure availability of this data when it's needed.

$\rightarrow$ The accuracy is more important than speed in the ETL Process and  efficiency as well and to ensure efficient ETL process data is  fed through pipeline in smaller packets.
![[Pasted image 20250924142842.png]]

**Batch Processing VS Streaming Processing**
data is processed in batches on a repeating schedule or in periodic times but it can be also triggered by events as the following:
- data from source reaches a certain size
- any other event  of interest
- on-demand
Stream processing means that data is processed in immediately in real time.

> There is a trade-off between batch processing and stream processing in accuracy and latency where batch processing is more accurate but has high latency while stream processing is less accurate than batch processing but has low latency.

In order to fix that problem of high latency of batch processing there is another technique is used called **Tiny-batch pipelines** which is use batch processing but use small batches so it decrease the latency with high accuracy as batch processing.

**Hybrid-Lambda Architecture**
- is an architecture designed for handling big data.
- combine batch and streaming data pipelines techniques.
- Historical data is delivered in batches to the batch layer while the real time data is streamed to speed layer. These two layers are integrated in a serving layer.
- One of its drawbacks is the complexity in the logical design behind it.
- As an advantage of this architecture is the combining between speed and accuracy.


Tools for batch processing:
- pandas python: doesn't handle big data
- Apache Airflow: handles big data
Tools for stream processing:
- Apache Kafka
- Apache Spark


### Apache Airflow
#### What is Airflow
**Apache Airflow is a platform to programmatically author, schedule, and monitor workflows**
- Open-source orchestration tool.
- Used to build and run workflows.
- Workflow is represented as DAGs (Directed Acyclic Graphs).

#### Airflow Principles
- Scalable: Scale to infinity 
- Dynamic
- Extensible
- Lean: Elegant

#### Airflow Features
- Open-source
- Easy to use
- Useful UI
- Robust integration
- Pure python

#### Airflow Components
- **Scheduler**: decides **What** and **When**  to run.
- **Executor**: decides **Where** and **how** **to** run tasks.
- **Workers**: **actually do** the work of running tasks code .
- **DAG Directory**: contains all DAG files ready to be accessed by **Scheduler** and **Executor**.
- **Web Server**: Provide a GUI.


#### DAG
- Directed Acyclic Graphs
- No cycles in DAGs
- Nodes represents tasks and edges represent dependencies.
- Tasks are written in **Python**
- Tasks implement operators such as:
	- python code
	- Bash commands
	- SQL queries
	- Email or HTTP requests: Send emails

#### Python Script Blocks:
1. Import libraries
		`from airflow.models import DAG`
		`from airflow.operators.bash_operator import BashOperator`
		`from airflow.operators.python import PythonOperator`
		`from airflow.operators.email impot EmailOperator`
2. DAG arguments definition
		![[Pasted image 20250926170525.png]]
		`'started_date': days_ago(0)`: means that DAG should run from today.
		write your email to send  alerts.
		number of retries in case of  failure.
		time delay between retries.
	![[Pasted image 20250926170904.png]]
3. DAG  definition
	![[Pasted image 20250926171000.png]]
4. Task definition
	- Task is defined  by task id
	- dag it belongs to
	- actual task to be performed either python function, bash command or send email
5. Task pipeline
	![[Pasted image 20250926171227.png]]


#### Some problems i found when i installing Apache Airflow
1. Apache Airflow does not support python 3.12. To fix that:
	 - I made a new coda environment with python 3.10 and installed airflow in it but take care of dependencies
2. Airflow version 3.1 does not support the  command `airflow db init` so use `airflow db migrate`
3. Airflow version 3.1 does not support user creation so when you use `airflow standalone` it writes the username and password you should use to run airflow. The user name and password are in a json file in airflow directory.


#### Some airflow commands
- `airflow dags list` : Shows all existing dags
- `airflow tasks list <dag_name>`: show all tasks in the <dag_name>
- `airflow dags pause <dag_name>`: pause a dag
- `airflow dags unpause <dag_name>`: unpause a dag