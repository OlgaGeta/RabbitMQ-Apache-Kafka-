import pika
import time
import os

# подключение к rabbitmq 
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

connection = pika.BlockingConnection(url_params)
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)

def receive_message(ch, method, properties, body):
    print('как будто получаем сообщение: ', body.decode('utf-8'))
    time.sleep(2)
    print('сообщение успешно обработано')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='hello',
                   on_message_callback=receive_message)

print("Waiting to consume")

channel.start_consuming()
