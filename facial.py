from flask import Flask, render_template, Response
from camera import VideoCamera
# import create_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/exec2')
def parse1():
#     response_data_collection = 
    print("Here")
    VideoCamera().save_to_dataset()
#     if response_data_collection != None:
#         print("Done with Collecting Data")
#     else:    
#         response_data_collection = "Couldn't able to create data files"
#     return render_template('index.html', alert='Done with Collecting Data')