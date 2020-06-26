from flask import Flask, render_template, request, Response
from templates import *
from database import *
from media_player import *
from webstreaming import *
from datetime import timedelta
from camera import VideoCamera

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=3) 

@app.route("/")
def home():
    url_get = request.args.get('content')
    #zihan - set video variable
    if url_get == 'set_video':
        return get_page(url_get)
    if url_get == 'more_info':
        return get_page('more_info')
    if url_get == 'view_data':
        return get_page('data_page')
    else:
        return get_page('')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera('LibertyMutualInsuranceCommercial.mp4')),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

