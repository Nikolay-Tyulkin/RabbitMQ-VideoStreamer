# import the necessary packages
from flask import Flask, render_template, Response
from camera import VideoCamera
from Utils.VideoBroker import VideoBroker
from flask import request

app = Flask(__name__)
videoBroker = VideoBroker()
videoBroker.startRecieving()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("HUY")
        if request.form.get('Send'):
            #Get text from textarea name="textToSound"
            text = request.form.get('text')
            print(text)
            #Send text to broker
    return render_template('index.html')

def gen(videoBroker):
    while True:
        #get camera frame
        frame = videoBroker.getImage()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(videoBroker),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)