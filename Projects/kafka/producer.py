from sys import *
import random
from kafka import KafkaProducer, KafkaConsumer
import json
import time
import requests

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v:json.dumps(v).encode('utf-8'))

for i in range(3):
    response = requests.get("https://reqres.in/api/users?page="+str(i+1), headers={'x-api-key': 'reqres-free-v1'})
    data = response.json()
    if not data:
        break 
    producer.send('demo-topic', data)
    print(f"Data Sent: {data}\n")
    time.sleep(random.randint(1,5))

producer.flush()
