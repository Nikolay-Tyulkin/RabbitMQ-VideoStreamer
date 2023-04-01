import cv2
from Utils.VideoBroker import VideoBroker
from Utils.TextBroker import TextBroker
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

videoBroker = VideoBroker()
textBroker = TextBroker()
textBroker.startRecieving()

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (720, 1280))
    videoBroker.sendImage(frame)
    time.sleep(0.5)
