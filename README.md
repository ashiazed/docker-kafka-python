# Docker Kafka

An example of how to use Kafka with python. 

Bring up the containers

```
make up
```

## Working with the Python app

Enter app container:
```
make enter
```

Run a producer:
```
python 1_producer_basic.py
```

Run a consumer:
```
python 5_consumer_basic.py
```

## Working with Kafka

Enter Kafka container:
```
make enter-kafka
```

Make topic
```
kafka-topics --bootstrap-server kafka:29092 --create --replication-factor 1 --partitions 1 --topic demo
```

List current topics:
```
kafka-topics --bootstrap-server kafka:29092 --list
```

Start consumer and listen to topic
```
kafka-console-consumer --bootstrap-server kafka:29092 --topic demo
```

See kafka logs:
```
docker-compose logs kafka
```
