import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='trades')

# Log trades
def callback(ch, method, properties, body):
    print(f"Trade Log: {body.decode()}")

channel.basic_consume(queue='trades', on_message_callback=callback, auto_ack=True)

print("Trade Logger is running... Logging executed trades...")
channel.start_consuming()
