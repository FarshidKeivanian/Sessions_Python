import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='orders')

# Send an order
order = ' '.join(sys.argv[1:]) or "BUY 100 TSLA at $700"
channel.basic_publish(exchange='', routing_key='orders', body=order)

print(f"Order Sent: {order}")
connection.close()
