import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='chat_room')

message = ' '.join(sys.argv[1:]) or "Hello Chat Room!"
channel.basic_publish(exchange='', routing_key='chat_room', body=message)
print(f"Sent: {message}")
connection.close()