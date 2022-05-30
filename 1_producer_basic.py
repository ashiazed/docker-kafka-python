"""
A basic Kafka Producer

You'll need to have a `demo` topic already created.
You can start a consumer to listen to demo topic and run
this file.
"""
import structlog
from confluent_kafka import Producer

log = structlog.get_logger()

log.msg("Starting Kafka Producer")

# configure
properties = {
    'bootstrap.servers': 'kafka:29092',
}

# create Producer
producer = Producer(properties)

# send data
producer.produce('demo', 'hello world')

# flush and close the Producer
producer.flush()
