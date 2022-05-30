"""
A Kafka Producer that has a callback after it's done,
we're also producing data with specific key values

You'll need to have a `demo` topic already created.
For this project create 3 partitions.
You can start a consumer to listen to demo topic and run
this file.
"""
import time
import structlog
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer

log = structlog.get_logger()


def on_completion(err, msg):
    """
    Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush().
    """
    if err is not None:
        log.error(f'Message delivery failed: {err}')
    else:
        log.info(
            f'''Message delivered successfully.
            Partition: {msg.partition()}
            Key: {msg.key()}
            Topic: {msg.topic()}
            Offset: {msg.offset()}
            Timestamp: {msg.timestamp()}'''
        )


def main():
    log.msg("Starting Kafka Producer With Callback")

    # I tried this with a key/value serializer but that doesn't work with a
    # callback
    properties = {
        'bootstrap.servers': 'kafka:29092',
    }

    producer = Producer(properties)
    topic = 'demo'

    # send a bunch of data - asynchronous
    for i in range(10):
        value = f'hello world {i}'
        key = f'id_{i}'
        producer.produce('demo', value, key, callback=on_completion)

    # flush and close the Producer
    producer.flush()


main()
