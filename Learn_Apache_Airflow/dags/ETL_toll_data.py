from airflow import DAG

from airflow.providers.standard.operators.bash import BashOperator

from datetime import datetime, timedelta



args={

    'owner':'usfomar',

    'start_date':datetime(2025,  10, 10),#Start date is today days_ago(0) is not working in airflow 3.0

    'email':'yousefomar720@gmail.com',

    'email_on_failure':True,

    'email_on_retry':True,

    'retries':1,

    'retry_delay':timedelta(minutes=5)

}



with DAG(

    'ETL_toll_data',

    description='Apache Airflow Final Assignment',

    default_args = args,

    schedule=timedelta(days=1),

) as dag:

    


    #Task 1 Download the data from the internet

    download=BashOperator(

        task_id='download',

        bash_command='cd /opt/airflow/data;curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz -o tolldata.tgz'
        )
    
  

    #Task 2 extract files from .tgz file and store files in data directory

    unzip_data=BashOperator(

        task_id='unzip',
        #Create a new directory called ouput to store the output files in (tidy up the file hierarchy)
        bash_command='cd /opt/airflow/data;mkdir output;tar -xzf tolldata.tgz'

    )
    
    
    #Task 3 extract the needed data from the csv file
    extract_data_from_csv=BashOperator(
        #I use airflow in docker compose so i need to change directory first so i did.
        task_id='extract_csv',
        bash_command='cd /opt/airflow/data;cut -d "," -f1-4 vehicle-data.csv > output/csv_data.csv' 

    )
    
    
    #Task 4 extract the needed data or attributes from the tsv file
    extract_data_from_tsv=BashOperator(
        task_id='extract_tsv',

        #the default delimeter in cut command is the tab so i don't write it
        #i cares about columns from 5 to the end
        #i use translate to replace tabs by comma to make the comma separated file
        #remember that i am using airflow in docker compose
        bash_command='cd /opt/airflow/data;cut tollplaza-data.tsv -f5- | tr "\t" ","  > output/tsv_data.csv'

    )

    

    #Task 5 extract the needed attributes from the txt file
    extract_data_from_fixed_width=BashOperator(
        task_id='extract_txt',
        #i used -c option to cut from character number 59 which is i need 
        #to start from to the end  and replace all spaces by a comma to make it csv file
        bash_command='cd /opt/airflow/data;cut -c59- payment-data.txt | tr " " "," > output/fixed_width_data.csv'

    )


    #Task 6 collect the extracted data and merge them together in one .csv file
    consolidate_data=BashOperator(
        #Change the directory
        #Add the column names in the extracted file
        #Merge the three file in one file.csv using the paste command with a separator comma
        task_id='consolidate',
        bash_command='''cd /opt/airflow/data/output;
        echo "Rowid,Timestamp,Anonymized_vehicle_number,Vehicle_type,Number_of_axles,Tollplaza_id,Tollplaza_code,Type_of_payment_code,Vehicle_code" > extracted_data.csv;
        paste -d"," csv_data.csv tsv_data.csv > part1.csv;
        tr -d "\r" < part1.csv> part1-cleaned.csv;
        paste -d"," part1.csv fixed_width_data.csv >> extracted_data.csv;
        '''

    )
    
 

    

    #Task 7 transform data in the csv file (capitalize, edit the case something like that)

    transform_data=BashOperator(

        task_id='transform',

        bash_command='''cd /opt/airflow/data/ouptut;
        cat extracted_data.csv | tr [:lower:] [:upper:] > transformed_data.csv;'''

    )

    

    download >> unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data