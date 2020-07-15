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

from flask import Flask, Response, flash, request, redirect, url_for
import os
import appconfig as cfg
from templates import data_page, video_page, display_page, get_page, feature_page, eval_face
from datetime import timedelta
from camera import VideoCamera
from filestore import get_s3object, get_cvimage, gettemp_cvimage
from facedetect import facesquare, image_binary, get_fileext
from db_functions import get_data, insert_face
from werkzeug.utils import secure_filename
import base64

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = cfg.UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=3)
app.config['SECRET_KEY'] = cfg.SECRET_KEY

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

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed/<video_name>',methods=['GET'])
def video_feed(video_name):
    video_url = 'https://ohmypy-summer2020.s3.amazonaws.com/videos/' + video_name + '.mp4'
    return Response(gen(VideoCamera(video_url)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# this is a test for facial recognition
@app.route('/test')
def process():
    #this will search in the s3 for any files with the name steve and return top path
    image_path = get_s3object("Steve")
    #this transforms the image into a cv image for facedetect
    image = get_cvimage(image_path)
    output_array = image_binary(image, image_path)

    image_name = 'Steve Carell'
    insert_face(output_array["image"], image_name)
    return eval_face(output_array["html"], image_name, output_array["num_face"])


# learn face file upload handle
@app.route('/', methods=['POST','GET'])
def upload_file():
    name_in = '/' + request.form['name_in']
    uploaded_files = request.files.getlist("file")
    filename = ""
    output_array=[]
    test = 1
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

@app.route('/feature_pending')
def feature_pending():
    return feature_page()


@app.route('/upload_file',methods=['GET','POST'])
def select_file():
    name_in = "none"
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file_ext = get_fileext(file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if file_ext == 'jpg' or file_ext == 'png' or file_ext == 'jpeg':
                return redirect(url_for('uploaded_file', filename=filename, name=name_in))
    return redirect(url_for('feature_pending'))


# reroute after learn face
@app.route('/uploads/<filename>/<name>')
def uploaded_file(filename,name):
    filename = app.config['UPLOAD_FOLDER'] + "/" + filename

    image_file = gettemp_cvimage(filename)
    image = facesquare(image_file)
    output_array = image_binary(image, filename)

    insert_face(output_array["image"], name)
    return eval_face(output_array["html"], name, output_array["num_face"])


@app.route('/choose_file/<file_in>/<filetype>')
def choose_file(file_in,filetype):
    filename = app.config['UPLOAD_FOLDER'] + "/" + file_in

    image_file = gettemp_cvimage(filename)
    image = facesquare(image_file)
    output_array = image_binary(image, filename)

    #insert_face(output_array["image"], name)
    #return eval_face(output_array["html"], name, output_array["num_face"])
    return "1"

# initiate site
if __name__ == "__main__":
    app.run(debug=True)