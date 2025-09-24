#!/bin/bash

#Download the access file from web
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz"

#Unzip the file
gunzip -k web-server-access-log.txt.gz

#Replace # that separates between columns by ,
cat web-server-access-log.txt | tr "#" "," | cut -d"," -f1-4 > extracted-data.csv

echo "Data is extracted and transformed successfuly. It's ready for loading"
head extracted-data.csv

echo "Loading Process is started"

if cat extracted-data.csv | PGPASSWORD=usfomar psql -U postgres -h localhost  -d  template1 -c "Copy access_log From STDIN DELIMITER ',' CSV HEADER;"; then
	echo "Loading process is done"
	PGPASSWORD=usfomar psql -U postgres -h localhost  -d  template1 -c "Select * From access_log limit 20;"
else
	echo "Something wrong happened"
fi

echo "ETL Process is finished"
