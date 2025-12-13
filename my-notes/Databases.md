### Database Architecture

**Deployment Topology:** arrangements or configurations of hardware, software, and network components
**Choice of deployment topology depends on:**
- scalability
- performance
- reliability
- nature of application
**Common topologies**
1. **Single-Tier architecture:** 
	- All components on single server(user interface, application logic, data storage)
2. **Client-Server or two-tier architecture:** 
	- consists of two layers:
		1. Client Layer $\rightarrow$ for user interface.
		2. Server Layer $\rightarrow$ for application logic and data storage.
	- interface communicates with the server through API
3. Three-tier architecture:
	- limits access to database except administrators.
	- better performance (avoid overloading).
	- consists of :
		1. client layer
		2. application server
		3. database server
4. Cloud-Based
	- database resides in cloud environment

**DBMS Layers**
1. Access layer
2. Engine layer
3. Storage layer


### Distributed Architecture and Clustered Database

**Types of Database Architectures:**
1. Shared disk architecture.
	- Multiple database servers processing workloads concurrently.
2. Shared nothing architecture.:
	- Allow workloads through multiple nodes either with replication or partitioning techniques.
3. Combination and Specialized architectures.
		-  Combination of shared disk and shared nothing 


### Notes or things i may forget

- **Indexes** 
	- in database in default stores the primary key with a pointer that points to the location of each row. so when you wanna search about a specific row it uses binary search in that index in O(log n) instead of O(n) and go for that location of that index and return it.
	- It improves the performance of retrieving data by minimizing disk scans.
	- One of the disadvantages is the usage of disk space. Decreased performance of insert, update, delete queries.


### MySQL load, restore and backup
- To open interactive mode of MySQL:
		`sudo mysql -u <username> -p<password>`
- To Load a MySQL script you can use the command **Source file_name**
- To back up a database to a .sql file 
	1. exit the interactive mode
	2. use mysqldump
		1. `sudo mysqldump -u <username> -p<password> <databases_name> > <backup_file_name.sql>`

### Design a Database
**There are three critical phases in the process of designing a database**
1. Requirement Analysis:
	- Gather information from stakeholders what are they want
	- You need to identify the main objects of the database such as (tables, attributes, relationships, ...).
	- Most of times the output was a report, presentation, or diagrams.
2. Logical Design:
	- Transfer the output of requirement analysis into entities, attributes and relationships without any technical details
3. Physical Design