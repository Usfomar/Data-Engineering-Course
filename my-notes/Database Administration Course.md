### Lab: Automating Tasks in MySQL using Shell Scripts
#### Objectives
- Create a shell  script to backup the database
- Create a cron job to schedule the script
- Truncate the tables in the database
- Restore the database using script file


**What i need to perform this**:
1. Knowing how  to backup a database using mysqldump
	- `mysqldump` `[Option]` > backup-file.sql
2. zip the backup file using `gzip` command
3. After a month delete the backup files.
		using `find` command with `-mtime` `-delete` option 

`find path -mtime +7 -delete` :
- mtime tells find command to search for files that  last modified date (only its contents) within this period of time with default  unit is days:
	- +n $\rightarrow$ files that are modified more than n days
	- -n $\rightarrow$ files that are modified less than n days
	- n  $\rightarrow$ files  that are modified exactly in n days
- - delete tells find to delete the files  that matches the search condition