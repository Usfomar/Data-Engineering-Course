### Objectives
1. Extract data from various sources with different formats (csv,tsv).
2. Transform these data and store it as a single file.
3. Load the data in a staging area for future use.
4. Use apache airflow with Bash Operators to create a pipeline that perform that.


>[!Note]
>To  run a shell script in dag file in apache airflow environment  you should take care of the following:
>in the bash operator task you should add an additional space after the command for example:
>`bash_command='/opt/airflow/data/script.sh '` there is an additional space after `script.sh`
>Something else is you should write the absolute path of the shell script to prevent any unusual behaviors.

