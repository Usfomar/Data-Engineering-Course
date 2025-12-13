### What is Big Data? 
_Data generated in huge volumes and could be structured, semi-structured or unstructured data. It needs processing to generate insights for human consumption. It is generated at enormous speed **(grows exponentially)** from multiple sources with different data types._
- _Big data is distributed on cloud and server farms_/
### Characteristics of Big Data (The 5 V's of Big Data)
- **_Volume_**: Large amount of data.
- **_Variety_**: Different data types.
- **_Velocity_**: Data is generated on enormous speed.
- **_Veracity_**: The quality, accuracy or trustworthiness of data.
- **_Value_**: The utility or the insights can be derived from the data once it has been analyzed.
### Hadoop
_Hadoop plays a major role in open source big data industry. Hadoop is an ecosystem that combine a collection of programs that support working in big data clusters_ .

**_Three major components of Hadoop Ecosystem_**:
1. **Hadoop Common**: Refers to the common utilities and libraries that support the other Hadoop modules.
2. **Hadoop Distributed File System (HDFS):** The file system that manage and store Big data files.
3. **Hadoop MapReduce**
4. **Yet Another Resource Negotiator (YARN)**: Resource manager.

> Big data which Hadoop used for storing, managing and analyzing it are stored in independent nodes and these nodes communicating with each other through secure protocol.  

>[!NOTE]
Nodes are computers

**_In Hadoop Ecosystem, There are two types of nodes_**:
1. **Namenode**: is the node the user interacts with and it's the node which know the topology of the cluster and know where the data the user querying on in which data node
2. **Datanodes**: Nodes that store, process big data and the nodes contains the computation power.
#### Steps for Big Data Processing
1. **Ingest Data**: 
	- Get data from multiple sources, aggregate and transform it before storing process.
	- Using tools like Flume, Sqoop
2. **Store Data**:
	- Store transformed  data in HDFS across  the cluster of nodes.
	- Tools such as **HBase** is a non-relational database that runs on top of HDFS and it provides real time data wrangling. **Cassandra** is also a No SQL database and it's known for its ability of remains available.
3. **Analyze Data**:
	- **Pig**: Operates  on the client side on the server, it's a procedural data flow language.
	- **Hive**: Used for creating reports, operates on the server side of a cluster. It's a declarative programming language
4. **Access Data**
	- The step the user will access the analyzed data.
	- Tools like **Impala** are often used, which does  not need any programming skills.
	- **Hue** can be used too.

#### Lets Talk About Hive
**Hive** is a data warehouse software withing Hadoop. It's designed for reading, writing and managing tabular-type datasets and data analysis.

**Characteristics of** **Hive**
1. Scalable, fast and easy to use.
2. Hive Querying Language HQL is based on SQL so it looks like SQL.
3. Supports data cleansing and filtering.

**Compare Between Traditional RDBMs and Hive**

| Traditional RDBMs                                                                            | Hive                                                              |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Used to maintain a database and use SQL                                                      | Used to maintain a data warehouse using HQL (Hive Query Language) |
| Suited for dynamic/real-time data came from sensors                                          | Suited for static data analysis  such as text files               |
| Designed for many writes and reads operations (Allow many Insert, Update, Delete Operations) | Designed for Write once and Read many times.                      |
| Handles up to Terabytes of data                                                              | Handles up to Petabytes of data                                   |
| Does not support built-in data partitioning                                                  | Supports data partittioning                                       |

#### Hive Architecture
**Three Main Parts:
1. **Hive Client:** is depending on the application which use Hive even it was java based applications Hive use JDBC Driver, and for other applications Hive use ODBC driver. These drivers communicates with the Hive server.
2. **Hive Server**: Any queries are done here.
3. **Hive Storage and Computing**: Metadata, query results and data loaded in the tables are stored in Hive Storage Part.

![[Pasted image 20251125162459.png]]