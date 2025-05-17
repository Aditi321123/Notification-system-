import pika, json
from workers.email_handler import send_email
from workers.sms_handler import send_sms
from workers.inapp_handler import send_inapp

def callback(ch, method, properties, body):
    data = json.loads(body)
    try:
        notif_type = data['type']
        if notif_type == 'email':
            send_email(data)
        elif notif_type == 'sms':
            send_sms(data)
        elif notif_type == 'inapp':
            send_inapp(data)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Failed: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='notifications')
channel.basic_consume(queue='notifications', on_message_callback=callback)
print("Worker started. Waiting for messages...")
channel.start_consuming()
