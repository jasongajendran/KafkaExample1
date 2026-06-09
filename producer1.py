from kafka import KafkaProducer
from typing import Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_producer(bootstrap_servers: list = None) -> KafkaProducer:
    """
    Create and return a KafkaProducer instance.

    Args:
        bootstrap_servers: List of Kafka broker addresses.
                          Defaults to ['localhost:9092']

    Returns:
        A configured KafkaProducer instance
    """
    if bootstrap_servers is None:
        bootstrap_servers = ['localhost:9092']

    return KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: v.encode('utf-8')
    )


if __name__ == "__main__":
    producer = create_producer()
    topic = 'ecommerce_orders'

    print('Type messages to send to Kafka. Enter CTRL+C or type "quit" to exit.')

    try:
        while True:
            message = input('Message: ').strip()
            if not message or message.lower() == 'quit':
                logger.info('Exiting producer.')
                break

            future = producer.send(topic, value=message)
            record_metadata = future.get(timeout=10)

            logger.info(f'Sent message to {record_metadata.topic} '
                       f'partition {record_metadata.partition} '
                       f'offset {record_metadata.offset}')
            producer.flush()
    except KeyboardInterrupt:
        logger.info('Keyboard interrupt detected. Exiting producer.')
    finally:
        producer.close()
        logger.info('Producer closed.')

    