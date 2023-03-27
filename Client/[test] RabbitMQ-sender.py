
import pika
import sys
import cv2
import numpy as np
import base64
import time

image = cv2.imread(r'./Client/1L.jpg')
print(image.shape)
image = cv2.resize(image, (480, 480))
image = cv2.imencode('.jpg', image)[1]
image = base64.b64encode(image)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='84.201.177.253'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = image
for i in range(100):
    time.sleep(0.1)
    channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent Done!" )
connection.close()




