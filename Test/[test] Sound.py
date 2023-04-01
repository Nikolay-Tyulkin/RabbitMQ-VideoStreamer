
# Import the gTTS module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 

# It is a text value that we want to convert to audio 
text_val = "текст для перевода в аудио"
 
# Here are converting in English Language 
language = 'ru' 
 
# Passing the text and language to the engine, 
# here we have assign slow=False. Which denotes 
# the module that the transformed audio should 
# have a high speed 
obj = gTTS(text=text_val, lang=language, slow=False) 
#Here we are saving the transformed audio in a mp3 file named 
# exam.mp3 
obj.save("/home/pi/RabbitMQ-VideoStreamer/exam.mp3") 
 
import os
import subprocess

proc = subprocess.Popen(['mpg321', '/home/pi/RabbitMQ-VideoStreamer/exam.mp3'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
q = proc.communicate()[0]
print("gfd")