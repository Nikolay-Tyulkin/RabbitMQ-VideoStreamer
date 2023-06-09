import pika
import cv2
import numpy as np
import base64
import threading 
from Utils.Sound import Sound


class TextBroker:
    def __init__(self, host="84.201.143.216", exchange="video-streamer-text", exchange_type="fanout"):
        self.host = host
        self.exchange = exchange
        self.exchange_type = exchange_type

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type)
        self.textBuffer = None

    def close(self):
        self.connection.close()

    def startRecieving(self):
        self.recievingThread = threading.Thread(target=self.recieveText)
        self.recievingThread.start()

    def recieveText(self):
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        self.channel.queue_bind(exchange=self.exchange, queue=queue_name)

        #print(' [*] Waiting for logs. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            text = body.decode("utf-8")
            self.textBuffer = text
            if text == "":
                return
            print(text)
            sound = Sound()
            sound.playSound(text)
            self.textBuffer = None

        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        self.channel.start_consuming()

    def sendText(self, text):
        text = text.encode("utf-8")
        self.channel.basic_publish(exchange=self.exchange, routing_key='', body=text)
        