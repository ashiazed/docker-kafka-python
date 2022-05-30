"""
A Kafka Producer that has a callback after it's done

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
            Topic: {msg.topic()}
            Offset: {msg.offset()}
            Timestamp: {msg.timestamp()}'''
        )


if __name__ == '__main__':
    log.msg("Starting Kafka Producer With Callback")

    # I tried this with a key/value serializer but that doesn't work with a
    # callback
    properties = {
        'bootstrap.servers': 'kafka:29092',
    }

    producer = Producer(properties)

    # send a bunch of data - asynchronous
    for i in range(10):
        producer.produce('demo', value=f'hello world {i}', callback=on_completion)

        # Optionally sleep for a bit, this way you'll see data going into
        # multiple partitions
        time.sleep(1)

    # flush and close the Producer
    producer.flush()
