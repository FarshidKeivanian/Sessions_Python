import pika

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='trades')

# Callback function to log executed trades
def callback(ch, method, properties, body):
    print(f"Trade Log: {body.decode()}")

channel.basic_consume(queue='trades', on_message_callback=callback, auto_ack=True)

print("Trade Logger is running... Logging executed trades...")
channel.start_consuming()
