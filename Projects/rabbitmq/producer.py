#!/usr/bin/python3

import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue of name 'hello'
channel.queue_declare(queue='hello') # durable, queue will survive even after restart
channel.queue_declare(queue='misc')

# now publish

for i in range(5):
    time.sleep(random.randint(1,5))
    channel.basic_publish(exchange='', routing_key='hello', body='Hello Message: '+ str(i))
    time.sleep(random.randint(1,5))
    channel.basic_publish(exchange='', routing_key='misc', body='Misc Message: '+ str(i))
    print("Message Published")

# flush
connection.close()



