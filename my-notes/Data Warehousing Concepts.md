### Objectives
- Data cubes and its operations.
- Materialized views
- Star Schema Vs Snowflake Schema
-  Slowly Changing Dimensions (SCDs)
---

#### Data cube operations:
1.  **Slicing**: The process of taking one slice or selecting a single member of a dimension with yields to data that has one dimension less than the original cube.
2. **Dicing**:  Selecting a subset of values from a dimension.
3. **Drilling** **up**: in snowflake schema, you will find hierarchies or subcategories within some of the dimensions
4. **Drilling** **down**: is the reverse of drilling up.
5. **Pivoting**: A rotation of data cube dimensions.
6. **Roll up**: Summarized a dimension
#### Materialized Views: 
- A read-only snapshot containing the result of a query. It used to replicate data or precompute expensive queries for a data warehouse.
- Automatically keep query result synced to database.
- Create physical table contains the result of a query.
- Faster than to query than the base tables.
- It uses in data warehousing where data is large and performance is important especially complex queries.
- Different refresh options:
	1. Never
	2. Upon  request: can done either manually or on a schedule
	3. Immediately.
- Materialized View Creation
	`Create Materialized View  <view_name> As (Select Statement);`
- As we know  that the materialized is not automatically updates  the changes so you need to refresh it before using if needed:
	`Refresh Materialized View <view_name>;`
#### Star VS Snowflake Schemas
1. **Star Schema**
	- Means that data tables are shaped as star when fact table has connection to dimension tables using foreign keys.
	- Used  for specialized Data warehouses which are Data Marts.
2. **Snowflake Schema**
	- Is the generalization of Star Schema or normalized Star Schema.
	- Dimension tables are split into child tables.
	- Needn't to be fully normalized to be considered a snowflake schema.

#### Slowly Changing Dimensions (SCD)

Are method to monitor the changes in the dimension attributes, manage updates, helping business preserve the historical data.

Various types of SCDs:
1. **Type 0 (Retain Original Value)** 
	- Means dimension is static which once a value is inserted it will remain static.
2. **Type 1(Overwrite the existing  data)**
	- Means that if attribute is changed the change will overwrite the old value.
	- No historical data is retained.
3. **Type 2 (Preserve Historical Data or Row versioning)**
	- When a record in a dimension changes it creates new row with the new value with keeping the old record but label old record as it's historical.
4. **Type 3 (Add New Attribute)**
	- If a record column is changed a new attribute with the new value is created with preserving the old value.
	- Good at small  amount of changes.
5. **Type 4 (Historical Table)**
	- Historical data is stored in separated table from the current dimension table.
6. **Type 6 (Hybrid Approach)**


#### Populating  a Data Warehouse
1. Create the structure of the data warehouse (Create the  fact table and dimension tables).
2. Define the relationships between fact and dimension tables.
3. Loading the  initial load to the data warehouse.
4. Automate the incremental loads either when changes are happened or schedule the loading times.
5. Finally, apply periodical maintenance and verification most of times  monthly or yearly according to the nature of your data warehouse.


#### Data Warehousing Final Project
##### Objectives
1. Design a data warehouse (dimension tables, fact table).
2. Create the data warehouse.
3. Load data into the data tables.
4. Transform loaded data to be clean and conforms the requirements.
5. Create materialized view to simplify complex queries.
6. Perform data analysis through some queries. 


##### Things i used to implement the project (Revision)
1. Alter data  type of table
	`Alter Table <table_name> Alter Column <column_name> Type <new_data_type>`
2. Alter table to add foreign keys
	`Alter table <table_name> Add Constraint <constrain_name> Foreign Key (column_name) References <table_name>(column_name) ON DELETE SET NULL or CASCADE`
3. Import data from csv  file into postgreSQL table
	`Copy <table_name> From <file_full_path> Delimiter ',' Header`
	- Header means  that the file contains the headers so ignore the first line
	- Delimiter could be changed to tab or another types of delimiters
	- you can replace the file full path by STDIN which is used with the pipeline in the command for example:
		`cat file.csv | psql -U postgres -h localhost <database> -c 'Copy <table_name> From STDIN Delimiter "," Header'`



### Final  Project 

#### Dimension Date Columns
1. date_id
2. date
3. year
4. quarter
5. quarter_name
6. month
7. month_name
8. day
9. weekday
10. weekday_name



| Dimension Date | Dimension Station | Dimension Truck | Trips (Fact Table) | Dimension Waste | Dimension_Zone |
| -------------- | ----------------- | --------------- | ------------------ | --------------- | -------------- |
| date_id        | station_id        | truck_id        | trip_id            | waste_id        | zone_id        |
| date           | city              | truck_type      | date_id            | waste_type      | zone_name      |
| year           |                   |                 | station_id         |                 | city           |
| quarter        |                   |                 | truck_id           |                 |                |
| quarter_name   |                   |                 | waste_collected    |                 |                |
| month          |                   |                 |                    |                 |                |
| month_name     |                   |                 |                    |                 |                |
| day            |                   |                 |                    |                 |                |
| weekday        |                   |                 |                    |                 |                |
| weekday_name   |                   |                 |                    |                 |                |
