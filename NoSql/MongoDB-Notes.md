## MongoDB Shell Commands

### Basic Commands

1. Login to MongoDB with username and password:
   `mongosh -u <username> -p <password>`
2. To show all databases:
   `show dbs`
3. Use a database and if it's not found it creates it:
   `use <database_name>`
4. Create a new collection:
   `db.createCollection("<collection_name>")`
5. List all collections in a database:
   `show collections`
6. Insert documents in a collection:
   `db.collection.insert({'key':'value'})`
7. Count the number of documents in a collection:
   `db.collection.countDocuments()`
8. Display all documents in a collection:
   `db.collection.find()`
9. Drop a collection:
   `db.collection_name.drop()`

### Indexes in MongoDB

- Indexes in MongoDB are stores as a balanced binary tree
- It's reformat the order of the data based on the key the index made on, each value of the key corresponds to a pointer that points to the document in the memory

- Create Index: `db.collection.createIndex({'key':1})`
  - 1 means that the index sort the values of the key ascending
  - -1 for descending order
- List all indexes in the collection: `db.collection.getIndexes()`
- Drop an Index: `db.collection.dropIndex({'key':1})`

### Aggregation

Most Commong Aggregation You Can Use:

- $group you should use one of these with it ($avg, $min, $max,$sum,...)
- $limit
- $sort either ascending sort is 1 or descending is -1
- $match
