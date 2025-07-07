import socket
import time
import random

HOST = "0.0.0.0"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    id = random.randint(1,10)
    while True:
        text = "Hello There! I am client ["+str(id)+"]"
        s.sendall(text.encode('utf-8'))
        data = s.recv(1024)
        time.sleep(10)
        print(f"Received {data}")
