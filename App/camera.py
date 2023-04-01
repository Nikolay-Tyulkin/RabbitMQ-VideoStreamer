# import the necessary packages
import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6
class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()

    def get_frame(self):
        #extracting frames
            ret, frame = self.video.read()
            frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
            interpolation=cv2.INTER_AREA)                    
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face_rects=face_cascade.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in face_rects:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                break
            # encode OpenCV raw frame to jpg and displaying it
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
# Test script
# cam = VideoCamera()
# while True:
#     frame = cam.get_frame()
#     # frame to numpy
#     frame = np.fromstring(frame, dtype=np.uint8)
#     frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break