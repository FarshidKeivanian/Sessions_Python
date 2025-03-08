def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")

channel.basic_consume(queue='chat_room', on_message_callback=callback, auto_ack=True)
print("Waiting for messages. Press CTRL+C to exit.")
channel.start_consuming()