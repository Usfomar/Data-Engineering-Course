### Objectives
1.  Difference between MapReduce and Spark
2. Apache Spark Setup
3. Create a Spark Session and Spark Context
4. Design the schema of a Data Frame
5. Convert pandas data frame into a spark data frame
6. Create a  spark data frame from a json and csv files


> [!Note  That]
> Spark is written in Scala  programming language and runs in JVMs (Java Virtual Machines).

#### Difference  Between MapReduce and Spark
The main difference between them that ***MapReduce*** each time needs to apply some operations on data it performs read and write operations on the data stored on the  disk (This  is time consuming), While ***Spark*** access the data once from the disk and caches it in the memory which makes processing so much faster than access it from the disk each time.

**Question**: What is **Spark SQL**?
Spark SQL is a spark module which used for processing structured data stored across nodes in a cluster

**Question**: What is  **SparkContext**?
![[Pasted image 20251129125629.png|300]]
**SparkContext** is the main  entry point for spark functionality. It  represents the connection to a spark cluster. It can be used to create **RDD**
	``sc = SparkContext(master='ClusterURL', appName='Name of application')

#### Spark Setup
1. Install `pyspark` and `findspark`
	- `pyspark` : Is the python API of  Spark
	- `findspark` : Is used to locate spark installation and allow us use its functions
2. Initialize a SparkSession
	![[Pasted image 20251128192604.png]]
3. Create a SparkContext
	`sc = SparkContext()` : you can use it for functions like `parallelize()` to create  an RDD 
	`RDD = sc.parallelize(data,4)` Means partition data into 4 partitions


#### Design a schema To Create a Spark Data Frame
`from pyspark.sql.type import StrurctType, FieldType, StringType, LongType`
![[Pasted image 20251128193131.png]]
**To Create  a spark data frame from a pandas data frame**
- first, you should ensure that  the fields in pandas data frame should be names similar to the schema we create and  the data type is matched as well.
	`spark_df = spark.createDataFrame(df[schema.FieldNames()])`
- **To print the  content of the  spark data frame**
	`spark_df.show()`
- **To display the schema to ensure it if something wrong** 
	`spark_df.printSchema()`

#### Create a Spark Data Frame from JSON and CSV files
> [!IMPORTANT]
> Designing a schema and use the defined schema when reading csv files in spark data frame makes the process of reading much faster than use options like `inferschema=True`, because without predefined schema spark will perform internally operations to discover the  right schema of the file and this is time and resource consuming.

1. **From JSON file**
	`spark_df = spark.read.json('file.json')`
2. **From CSV file**
	1. Design the schema (fields, data types, if null allowed or not)
	2. `df = spark.read.format('csv').option('header','true').schema(my_schema).load('file_path.csv')`
	3. `df = spark.read.csv('file.csv',header=True,inferschema=True)`
		- `inferschema=True`: is not the best way
			- design the schema first then `schema=my_schema`