#!/bin/bash

#Extract data from the file
filename="/home/omar/Data-Engineering/ETL/passwd.csv"

cat /etc/passwd | cut -d":" -f1,3,6 | $filename
tr ":" "," < $filename > $filename
echo "After extraction and Transformation"
head -5 $filename



#Load data into a PostgreSQL table in templete1 database called users
if cat $filename | PGPASSWORD=usfomar psql -U postgres -h localhost -d template1 -c "Copy users From STDIN With (Format csv);";then
	echo "Table is imported Successfullu"
	PGPASSWORD=usfomar psql -U postgres -h localhost -d template1 -c "Select * From users Limit 10;"
else
	echo "Something Wrong happend"
	exit 1
fi

