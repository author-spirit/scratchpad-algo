from sys import *
from kafka import KafkaConsumer
import json

"""
earliest: Consume all existing messages
latest: Get only new, ignore old ones
"""

consumer = KafkaConsumer('demo-topic', 
    bootstrap_servers=['localhost:9092'], 
    auto_offset_reset='earliest',
    value_deserializer=lambda m:json.loads(m.decode('utf-8'))
)

print("Demo-Topic: Consuming....")

for message in consumer:
    print(f"Received: {message.value}\n")
