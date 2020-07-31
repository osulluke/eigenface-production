##################################################
## FileName: main.py
##################################################
## Author: RDinmore, XWu
## Date: 2020.06.22
## Purpose: server main page
## Libs: flask, datetime
## LocalLibs: templates, database, camera, filestore
## Path: Flask_UI/filestore
##################################################

from flask import Flask,  flash, request, redirect
import os
import appconfig as cfg
from templates import data_page, video_page, display_page, get_page, feature_page, eval_face, basic_video
from datetime import timedelta
from facedetect import facesquare, image_binary, get_fileext, video_face_rec
from lib import *
#from lib.sub_process_test import run_face_screener
from werkzeug.utils import secure_filename
from multiprocessing import Process

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = cfg.UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=3)
app.config['SECRET_KEY'] = cfg.SECRET_KEY
#face_detection = Process(target=run_face_screener)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    url_get = request.args.get('content')
    video_get = request.args.get('video_name')

    if url_get == 'database':
        return data_page(get_data())
    elif url_get == 'data_page':
        return video_page(video_get)
    elif url_get == "uploads":
        return display_page(video_get)
    else:
        return get_page(url_get)


# learn face file upload handle
@app.route('/', methods=['POST','GET'])
def upload_file():
    uploaded_files = request.files.getlist("file")
    output_array=[]
    route = 0

    for file in uploaded_files:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                break
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                route = 1
                break
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                basedir = os.path.abspath(os.path.dirname(__file__))
                file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
                image_file = gettemp_cvimage(app.config['UPLOAD_FOLDER'] + "/" + filename)

                image = facesquare(image_file)
                output_array = image_binary(image, app.config['UPLOAD_FOLDER'] + "/" + filename)

                if image["num_face"] == 1:
                    insert_face(image["gray_im"], request.form['name_in'])
                route = 2

    if route == 0:
        flash('No file part')
        return redirect(request.url)
    elif route == 1:
        flash('No selected file')
        return redirect(request.url)
    elif route == 2:
        return eval_face(output_array["html"], request.form['name_in'], output_array["num_face"])


# reroute after learn face
@app.route('/uploads/<filename>/<name>')
def uploaded_file(filename,name):
    filename = app.config['UPLOAD_FOLDER'] + "/" + filename

    image_file = gettemp_cvimage(filename)
    image = facesquare(image_file)
    output_array = image_binary(image, filename)

    insert_face(image["gray_im"], name)
    return eval_face(output_array["html"], name, output_array["num_face"])


@app.route("/basic_video", methods=['GET'])
def play_vid():
    return basic_video()


# initiate site
if __name__ == "__main__":
    #face_detection.start() # Begin the face detection algorithm
    app.run(debug=True) # Start the webserver
    #face_detection.kill() # End the face detection algorithm
