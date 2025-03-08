def callback(ch, method, properties, body):
    print(f"Tracking: {body.decode()}")

channel.basic_consume(queue='position', on_message_callback=callback, auto_ack=True)
print("Tracker is running...")
channel.start_consuming()