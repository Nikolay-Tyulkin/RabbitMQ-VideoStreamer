
import pika
import sys
import cv2
import numpy as np
import base64
import time



connection = pika.BlockingConnection(pika.ConnectionParameters(host="84.201.143.216"))
channel = connection.channel()

channel.exchange_declare(exchange='video-streamer', exchange_type='fanout')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (100, 100))
    frame = cv2.imencode('.jpg', frame)[1]
    frame = base64.b64encode(frame)
    message = frame

    channel.basic_publish(exchange='video-streamer', routing_key='', body=message)
    #print(" [x] Sent Done!" )
connection.close()


