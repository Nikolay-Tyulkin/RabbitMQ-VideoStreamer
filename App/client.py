import cv2
from Utils.VideoBroker import VideoBroker
from Utils.TextBroker import TextBroker
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

videoBroker = VideoBroker()
textBroker = TextBroker()
textBroker.startRecieving()

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (100, 100))
    videoBroker.sendImage(frame)
