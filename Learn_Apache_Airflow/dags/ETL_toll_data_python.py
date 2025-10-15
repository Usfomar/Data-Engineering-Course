import requests
import pandas as pd
import tarfile
import os
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator
from airflow.models import DAG

main_path='/opt/airflow/data/'


#Function that download the .tgz file and unzip it
def download_unzip():
    file_name = main_path+'tolldata.tgz'  #declare the file.tgz name
    if os.path.exists(main_path+'output'):
        os.system(f'rm -r {main_path}output')
        os.mkdir('output')
    else:
        os.mkdir(main_path+'output')
        
    #download the file using requests lib
    response = requests.get('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz')
    if response.status_code == 200:
        with open(main_path+'tolldata.tgz', 'wb') as file:
            file.write(response.content)
    else:
        print("Something Wrong Happened")
        
    #Unzip the tar file to a directory data_files
    try:
        with tarfile.open(file_name,'r:gz') as tar:
            tar.extractall(main_path+'source_files')
    except tarfile.ReadError as e:
        print(f"Cannot read tar file: {e}")
    except FileNotFoundError as e :
        print(f"{file_name} is not found: {e}")
    except :
        print(f"Something Wrong happend")
    finally:
        print(f"File extracted successfully")

#Extract From csv
def extract_csv_data():
    csv_df=pd.read_csv(main_path+'source_files/vehicle-data.csv',header=None)
    col_names = ['Rowid','Timestamp','Anonymized_vehicle_number','Vehicle_type','Number_of_axles','Vehicle_code']
    #Add column names 
    csv_df.columns=col_names
    extracted_csv=csv_df[['Rowid','Timestamp','Anonymized_vehicle_number','Vehicle_type']]
    extracted_csv.to_csv(main_path+'output/csv_data.csv',index=False)

#Extract from tsv
def extract_tsv_data():
    #replace tab separator file to comman separator file called tsv_data.csv
    with open(main_path+'source_files/tollplaza-data.tsv', 'r') as file:
        with open(main_path+'output/tsv_data.csv','w') as output:
            output.write(file.read().replace('\t',','))

    tsv_df = pd.read_csv(main_path+'output/tsv_data.csv',header=None)
    col_names = ['Rowid','Timestamp','Anonymized_vehicle_number','Vehicle_type','Number_of_axles','Tollplaza_id','Tollplaza_code']
    tsv_df.columns=col_names
    tsv_df = tsv_df[['Rowid','Number_of_axles','Tollplaza_id','Tollplaza_code']]
    tsv_df.to_csv(main_path+'output/tsv_data.csv',index=False)

#Extract from txt
def extract_fixed_width_data():
    row_id=[]
    payment_type=[]
    vehicle_code=[]
    with open(main_path+'source_files/payment-data.txt','r') as input:
        for line in input: 
            # extract only what we needs which are the last two columns and convert it to csv file
            transformed_line = line.strip().replace(' ',',')
            # output.write()
            ls=transformed_line.split(',')
            row_id.append(ls[0])
            payment_type.append(ls[-2])
            vehicle_code.append(ls[-1])#to remove the addition \n which is added after split
    
    dictionary={
        'Rowid':row_id,
        'Payment_type':payment_type,
        'Vehicle_code':vehicle_code
    }                
    fixed_df=pd.DataFrame(dictionary)
    fixed_df.to_csv(main_path+'output/fixed_width_data.csv',index=False)

#Combine and unifty data types
def consolidate():    
    csv_df = pd.read_csv(main_path+'output/csv_data.csv')
    tsv_df = pd.read_csv(main_path+'output/tsv_data.csv')
    fixed_width_df = pd.read_csv(main_path+'output/fixed_width_data.csv')
    final_df=csv_df.merge(tsv_df,'inner', on=None).merge(fixed_width_df,'inner',on=None)
    final_df.to_csv(main_path+'output/extracted_data.csv',index=False)

#Transform final data file
def transform():
    final_df = pd.read_csv(main_path+'output/extracted_data.csv')
    final_df.Vehicle_type  = final_df['Vehicle_type'].apply(lambda x : x.upper())
    final_df.to_csv(main_path+  'output/transformed_data.csv',index=False)






args = {
    'owner': 'usfomar',
    'start_date':datetime(2025,10,13),
    'retries':1,
    'retry_delay':timedelta(seconds=5)
}

dag = DAG(
    dag_id='ETL_toll_data_python',
    default_args=args,
    schedule=timedelta(days=1),
    description='Airflow final project but using  python operator instead of bash operator',
        
)


download_and_unzip=PythonOperator(
    task_id='download_unzip',
    python_callable=download_unzip,
    dag=dag
)

csv_extraction=PythonOperator(
    task_id='extract_csv',
    python_callable=extract_csv_data,
    dag=dag
)

tsv_extraction=PythonOperator(
    task_id='extract_tsv',
    python_callable=extract_tsv_data,
    dag=dag
)

txt_extraction=PythonOperator(
    task_id='extract_fixed_width',
    python_callable=extract_fixed_width_data,
    dag=dag
)

consolidate_data=PythonOperator(
    task_id='consolidate',
    python_callable=consolidate,
    dag=dag
)




transform_data=PythonOperator(
    task_id='transform_data',
    python_callable=transform,
    dag=dag
)


#data pipeline

download_and_unzip >> csv_extraction >> tsv_extraction >> txt_extraction >> consolidate_data >> transform_data