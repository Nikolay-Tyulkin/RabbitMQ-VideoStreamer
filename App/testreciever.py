from Utils.Broker import Broker
import cv2
import time

broker = Broker()
broker.startRecieving()

while True:
    image = broker.getImage()
    if image is not None:
        cv2.imshow("test", image)
        cv2.waitKey(1)
    time.sleep(0.1)