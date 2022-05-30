"""
A Kafka Producer with a configured key and value serialization.

The SerializingProducer is actually still unstable,
and I'm not 100% sure it's necessary as the keys and values
for this yet.

You'll need to have a `demmo` topic already created.
You can start a consumer to listen to demo topic and run
this file.
"""
import structlog
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer

log = structlog.get_logger()

log.msg("Starting Kafka Producer")

properties = {
    'bootstrap.servers': 'kafka:29092',
    'key.serializer': StringSerializer('utf_8'),
    'value.serializer': StringSerializer('utf_8'),
}

# create the Producer (we need to use the SerializingProducer to
# be able to configure key and value
producer = SerializingProducer(properties)

# send the data - asynchronous
# we pass the value here explicitly as it's the 3rd arg not 2nd
producer.produce('demo', value='hello world')

# flush and close the Producer
producer.flush()
