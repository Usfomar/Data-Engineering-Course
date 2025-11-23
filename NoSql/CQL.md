## Cassandra Quering Language

### Data Types

Data types in Apache Cassandra are grouped in 3 main categories:

1. **Built-in Data Types**
2. **Collection Data Types**
3. **User Defined Data Types**

---

#### 1. Built-in Data Types

Commong data types such as (ASCII, int, double, float, decimal, text).
Another data types such as:

1. **Blob (Binary large Objects):** Is used for storing a small imageor short string (1 MB).
2. **Bigint:** Is used for storing 64-bit signed integers.
3. **Varchar:** Is used for storing UTF 8 encoded strings.

---

#### 2. Collection Data Types

> Collection data type is a way to group and store data together, for example if a user has more than one email, In relational database we create two tables users and emails and joins the two tables together, but in cassandra there is no joins, so you must enter the data joined. In the example of user emails use a list collection type to store all emails for that user. Collection data types should be limited.

Types of Collection Data Types:

1. **Lists:** Is used when order is important and allow duplicates.
2. **Maps:** Is a key-value pair data type.
3. **Sets:** Is a list but elements are unique and the order is important
