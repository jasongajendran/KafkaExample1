from kafka import KafkaConsumer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_consumer(topic: str = 'ecommerce_orders',
                    bootstrap_servers: list = None,
                    group_id: str = 'ecommerce_orders_consumer_group') -> KafkaConsumer:
    """
    Create and return a KafkaConsumer instance.

    Args:
        topic: Kafka topic to subscribe to
        bootstrap_servers: List of Kafka broker addresses.
                          Defaults to ['localhost:9092']
        group_id: Consumer group ID

    Returns:
        A configured KafkaConsumer instance
    """
    if bootstrap_servers is None:
        bootstrap_servers = ['localhost:9092']

    return KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=group_id,
        value_deserializer=lambda v: v.decode('utf-8')
    )


if __name__ == "__main__":
    consumer = create_consumer()
    logger.info('Listening for messages on topic "ecommerce_orders"...')

    try:
        for message in consumer:
            logger.info(f'Received message from {message.topic} '
                       f'partition {message.partition} '
                       f'offset {message.offset}: {message.value}')
    except KeyboardInterrupt:
        logger.info('Keyboard interrupt detected. Exiting consumer.')
    finally:
        consumer.close()
        logger.info('Consumer closed.')