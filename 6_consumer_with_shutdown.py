"""
A basic Kafka Consumer
It will consume demo topic, you can run it in conjunction
with 4_producer_with_keys.py to get data in before and during
This one catches keyboard interrups and closes consumer.
"""
import structlog
from confluent_kafka import Consumer

log = structlog.get_logger()

if __name__ == '__main__':
    log.msg("Starting Kafka Consumer")

    # configure
    properties = {
        'bootstrap.servers': 'kafka:29092',
        'group.id': 'my-other-application',
        'auto.offset.reset': 'earliest',
    }

    topic = 'demo'

    # create a consumer
    consumer = Consumer(properties)

    # Subscribe to topic
    consumer.subscribe([topic])

    try:
        # poll for new data
        while True:
            msg = consumer.poll(1)
            if msg:
                log.info(
                    f'''
                    Key: {msg.key()}
                    Value: {msg.value()}
                    Partition: {msg.partition()}
                    Offset: {msg.offset()}'''
                )
    except KeyboardInterrupt:
        log.info("Shutdown initiated")
    finally:
        consumer.close()
