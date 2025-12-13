### How to run apache kafka server
> You should do that every time you need to run kafka if the log directory is in `/tmp` directory so to get rid of that you can change the location of logs files of kafka by changing the path in `config/server.properties` of `logs.dir = any permanat path`
1. You need to generate new cluster id and export it
	`$ export KAFKA_CLUSTER_ID=$(bin/kafka-storage.sh random-uuid)`
2. You need to format the storage directory
	`$ bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties`
3. Run Kafka
	`$ bin/kafka-server-start.sh config/server.properties`


### Kafka Commands
1. Create or Delete a new topic
	`bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic <topic-name> --create or --delete`
2. To send message you should create a producer and start to pass message you wanna send or publish to a specific topic
	`bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic <topic-name>`
	this  opens something like a shell or a panel to pass your messages something like that:
	`> this is a message 1 
	`> this is a message 2 ` 
	you can pass a file of any format instead of passing message as an input from user you can do that by redirect an input file to the command
	`producer command < file.csv`
3. To read data sent from a producer you just wanna to subscribe to the topic that the producer sends data to and you can read the stream data or read the whole data from the beginning and you can read data to a new file as well
	`bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic-name> [Optional] --from-beginning > revieved-data.csv`

### Kafka-python API
#### Admin Client
-  `from kafka.admin import KafkaAdminClient, NewTopic`
	- `KafkaAdminClient`: manages topics it can create, delete, describe topics
	- `NewTopic`: is the class which is used when creating a new topic
- New topic creation:
	- `new_topic = NewTopic(name=<topic_name>, num_partitions=??, replication_factor=??)`
		- This creates a new topic with name of <topic_name> and it stores in number of partitions and you can also decide how many replication you wanna implement to that topic.
	- `topics=[].append(new_topic)` : this is made because admin client takes a list of topics to create the topics in it
	- Create an admin: `admin=KafkaAdminClient(bootstrap_servers='localhost:9092',client_id='test')`
	- Create list of topics : `admin.create_topics(new_topics=topics)`
- You can list all existing topics
	`admin.list_topics()`
- Describe a topic
	`admin.describe_topics(<topic_name>)`