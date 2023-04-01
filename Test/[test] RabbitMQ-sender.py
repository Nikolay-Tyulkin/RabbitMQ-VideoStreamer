
import pika
import sys
import cv2
import numpy as np
import base64
import time

image = cv2.imread(r'./Client/1L.jpg')
print(image.shape)
image = cv2.resize(image, (480, 680))
image = cv2.imencode('.jpg', image)[1]
image = base64.b64encode(image)

connection = pika.BlockingConnection(pika.ConnectionParameters(host="84.201.143.216"))
channel = connection.channel()

channel.exchange_declare(exchange='video-streamer', exchange_type='fanout')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (240, 160))
    frame = cv2.imencode('.jpg', frame)[1]
    frame = base64.b64encode(frame)
    message = frame

    channel.basic_publish(exchange='video-streamer', routing_key='', body=message)
    #print(" [x] Sent Done!" )
connection.close()


