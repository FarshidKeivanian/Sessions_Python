import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare both queues
channel.queue_declare(queue='orders')
channel.queue_declare(queue='trades')

# Process orders
def callback(ch, method, properties, body):
    order = body.decode()
    print(f"Processing Order: {order}")

    # Publish trade execution
    executed_trade = f"Trade Executed: {order}"
    channel.basic_publish(exchange='', routing_key='trades', body=executed_trade)

channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)

print("Exchange is running... Matching orders...")
channel.start_consuming()
