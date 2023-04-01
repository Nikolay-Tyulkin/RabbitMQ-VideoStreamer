import subprocess
import os
from gtts import gTTS 

class Sound:
    def __init__(self):
        self.fileBufferPath = "/home/pi/RabbitMQ-VideoStreamer/App/Utils/FileBuffer/"

    def playSound(self, text):
        obj = gTTS(text=text, lang='ru', slow=False) 
        obj.save(self.fileBufferPath + "exam.mp3") 
        proc = subprocess.Popen(['mpg321', self.fileBufferPath + "exam.mp3"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        q = proc.communicate()[0]
        os.remove(self.fileBufferPath + "exam.mp3")

    def playSoundFromFile(self, path):
        proc = subprocess.Popen(['mpg321', path], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        q = proc.communicate()[0]
