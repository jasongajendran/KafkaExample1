from kafka import KafkaProducer

def create_producer():
    return KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: v.encode('utf-8')
    )

producer = create_producer()
topic = 'ecommerce_orders'

print('Type messages to send to Kafka. Enter CTRL+C or type "quit" to exit.')

try:
    while True:
        message = input('Message: ').strip()
        if not message or message.lower() == 'quit':
            print('Exiting producer.')
            break

        future = producer.send(topic, value=message)
        record_metadata = future.get(timeout=10)

        print(f'sent message to {record_metadata.topic} partition {record_metadata.partition} offset {record_metadata.offset}')
        producer.flush()
except KeyboardInterrupt:
    print('\nKeyboard interrupt detected. Exiting producer.')
finally:
    producer.close()

    