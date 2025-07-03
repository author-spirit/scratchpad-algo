#!/usr/bin/env python
import pika
import os, sys

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    channel.queue_declare(queue='misc')

    def hello_cb(ch, method, properties, body):
        print("Hello queue: ", body)

    def misc_db(ch, method, properties, body):
        print("Misc queue: ", body)

    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=hello_cb)
    channel.basic_consume(queue='misc', auto_ack=True, on_message_callback=misc_db)

    print("Listening")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Terminated!")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
