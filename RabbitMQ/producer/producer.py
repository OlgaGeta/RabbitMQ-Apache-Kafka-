import pika
import os

# подключение к rabbitmq 
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

connection = pika.BlockingConnection(url_params)
chan = connection.channel()

chan.queue_declare(queue='hello', durable=True)

chan.basic_publish(exchange='', routing_key='hello',
                    body='Hello World', properties=pika.BasicProperties(delivery_mode=2))
                    
print("Produced the message")

chan.close()
connection.close()
