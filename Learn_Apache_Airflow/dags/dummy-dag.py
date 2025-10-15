from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.providers.standard.operators.bash import BashOperator


dag_args={
    
    'start_date':datetime(2025,10,4),#Means start from now,
    'retries': 2,
    'retry_delay':timedelta(seconds=10)    
}


with DAG(
    'dummy_dag',
    
    default_args=dag_args,
    description="Dummy DAG Does Nothing",
    schedule=timedelta(minutes=1)
    
) as dag:
    task1=BashOperator(
        task_id='task-1',
        bash_command='sleep 2'
    )
    
    task2=BashOperator(
        task_id='task-2',
        bash_command='sleep 4'
    )
    
  
  
    
    
    task1 >> task2