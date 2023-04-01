import pika
import cv2
import numpy as np
import base64
import threading 

class VideoBroker:
    def __init__(self, host="84.201.143.216", exchange="video-streamer", exchange_type="fanout"):
        self.host = host
        self.exchange = exchange
        self.exchange_type = exchange_type

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type)
        self.imageBuffer = None

    def close(self):
        self.connection.close()

    def startRecieving(self):
        self.recievingThread = threading.Thread(target=self.recieveImage)
        self.recievingThread.start()

    def recieveImage(self):
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        self.channel.queue_bind(exchange=self.exchange, queue=queue_name)

        #print(' [*] Waiting for logs. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            #print(" [x] image has been recieved")
            image = base64.b64decode(body)
            image = np.frombuffer(image, np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            self.imageBuffer = image

        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        self.channel.start_consuming()

    def getImage(self):
        image = self.imageBuffer
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    

        
