import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='position')

name = "Person1"
x, y = random.randint(0, 10), random.randint(0, 10)

while True:
    x = (x + random.choice([-1, 1])) % 10
    y = (y + random.choice([-1, 1])) % 10
    position = f"{name},{x},{y}"
    channel.basic_publish(exchange='', routing_key='position', body=position)
    print(f"Moved to: {position}")
    time.sleep(2)