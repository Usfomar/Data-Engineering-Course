**This contains any information needed  to implement the project included any details  i searched on to help me and any new tips and tricks that may make it  easier**

 > This project will be implemented through two RDBMSs which are PostgreSQL and MySQL.
 
#### To show all information of any table in MySQL database:
$\rightarrow$  All this info is stored in information_schema database:
- It contains information about tables, events, users, roles, engines, views and everything
		`Select TABLE_NAME, ENGINE, TABLE_SCHEMA, TABLE_ROWS, DATA_LENGTH FROM information_schema.TABLES;`

#### Project Objectives
- Installation/Provisioning
- Configuration
- User Management
- Backup

## 1. PostgreSQL

> In PostgreSQL database the concept of schema is critical and it's under the database level so one database can contain more than one schema unlike in MySQL which is schema represents or act as the database. So to show all schema in PostgreSQL in the database you are connecting use the following command `\dn`.


**We can copy the data from a .csv file to a database table in PostgreSQL by using `copy` command**
		`Copy schema.table From <absolute-path-of-file> With (Format csv)`
	We can use this also with linux pipelines instead of using the absolute path of the file we can do something like that:
		`cat file.csv | psql -U postgres -h localhost -d <database> -c "Copy schema.table From STDIN With (Format csv);"`


### User Management
#### 1. Create a User
	`Create User <username> With Password '<password>'`
#### 2. Create a Role
	`Create Role <role-name>;`
### 3. Grant Privileges to a Role
> [!Important]
> You Must Grant Usage On Database or Schema To Users or Roles Before Grant Any Types of Privileges.
> 	`Grant Usage On Schema <schema-name> To Role or User`


	`Grant <privileges_type> ON DATABASE <database_name> To <role-name>;`
- privileges such as (connect, select, insert, update, delete, alter, set, ...., All privileges)
	- All privileges gives all permissions to that role to do everything.
- To give privileges to a role to all tables in a schema use the following:
	`Grant Select on All Tables in Schema <schema-name> to <role-name>`

#### 4. Drop a Role
- Before you must remove everything that depends to that role by:
	`Drop Owned By <role-name>;`
- Now, you can drop it normally:
	`Drop Role <role-name>;`
#### 5. Grant and Revoke a Role to and From a user (Assign a role to a user)
	`Grant <role-name> To <user-name>`
	`Revoke <role-name> From <user-name>`


### 2. MySQL
**Objectives**
- Installation
- Configuration
- Recovery
- Indexing
- Storage Engines
- Automation of routine tasks

After installation and configuration of MySQL database called `billing` which is used in this project

First, we need to get more details about the tables in this database we'll do that through information_schema database using the following query:
	`Select TABLE_NAME, TABLE_SCHEMA, ENGINE,DATA_LENGTH FROM TABLES WHERE TABLE_SCHEMA='billing';`
- DATA_LENGTH: is the size of data file in bytes NOT the whole table size because of the size of index has its own column called `INDEX_LENGTH`.
- TABLE_SCHEMA: is the database where the table stored.

Now i implement `Select * from billdata;` And the question is how to improve the performance of that queries using indexes.
1. Instead of using * use column names `Select column1, col2, ... from billdata`
2. 