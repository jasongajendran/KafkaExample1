from kafka import KafkaConsumer

def create_consumer():
    return KafkaConsumer(
        'ecommerce_orders',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='ecommerce_orders_consumer_group',
        value_deserializer=lambda v: v.decode('utf-8')
    )

consumer = create_consumer()
print('Listening for messages on topic "ecommerce_orders"...')

try:
    for message in consumer:
        print(
            f'received message from {message.topic} '
            f'partition {message.partition} offset {message.offset}: '
            f'{message.value}'
        )
except KeyboardInterrupt:
    print('\nKeyboard interrupt detected. Exiting consumer.')
finally:
    consumer.close()