##################################################
## FileName: page_layouts.py
##################################################
## Author: RDinmore
# Date: 2020.06.22
# Purpose: return html to be displayed
# Libs: yattag, flask, urllib
## Path: Flask_UI/templates
##################################################

from yattag import Doc
from flask import url_for
import urllib.parse
import os
import sys
from lib import video_list
from pathlib import Path
import pandas as pd

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4'}


def get_page(page_name):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())

    if page_name == "data_page":
        doc.asis(view_data_page())
    elif page_name == "upload_files":
        doc.asis(upload_files())
    elif page_name == "choose_video":
        doc.asis(choose_video())
    elif page_name == "more_info":
        doc.asis(buttons())
        doc.asis(info_page())
    elif page_name == "learn_face":
        doc.asis(learn_face())
    else:
        doc.asis(buttons())

    doc.asis(footer())
    return doc.getvalue()


def data_page(datatable):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())
    with tag('div', id='container'):
        doc.asis('<span>This provides a view that our data API is actually working with; it will eventually provide more visibility in order to ensure data is uniform (correctly dimensioned, colored greyscale, etc).</span>')
        html = datatable.to_html()
        doc.asis(html)
    doc.asis(footer())
    return doc.getvalue()


def display_page(directory_in):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())
    display_image(directory_in)
    doc.asis(footer())
    return doc.getvalue()


def display_image(directory_in):
    doc, tag, text, line = Doc().ttl()
    with tag('div', id='photo-container'):
        doc.asis('<iframe width="1000" height="500" src="' + url_for('video_feed',
                                                                     video_name=directory_in) + '" frameborder="0" allowfullscreen></iframe>')
    return doc.getvalue()


def eval_face(response, image_name, output_count):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())
    doc.asis(footer())

    with tag('div', id='display_face'):
        with tag('div', id='photo-container'):
            doc.asis(response)
            doc.asis('</br>')
            doc.asis('</br>')
            if output_count == 1:
                text("Name: " + urllib.parse.unquote_plus(image_name))
                doc.asis('</br>')
                text("Face count: " + str(output_count))
                doc.asis('</br>')
            elif output_count > 1:
                text("Unable to add image, too many faces recognized")
            else:
                text("Unable to add image, no face recognized")
            doc.asis('</br>')
    doc.asis(footer())
    return doc.getvalue()


def info_page():
    doc, tag, text, line = Doc().ttl()
    with tag('div'):
        with tag('div', id='container'):
            with tag('div', id='display_info'):
                doc.asis(
                    '<div class="alert"><span class="closebtn" onclick="this.parentElement.style.display='+"'none'"+';">x</span>')
                text("This is a facial recognition media player. After selecting a media file the software will parse facial images and insert them into the database. ")
                text("These images will then be compared to current images and highlighted if recognized. The images will also be used to continue to grow the facial ")
                text("recognition data set.")
                doc.asis('</br></br>')
                text('At a high level, this project\'s purpose is to be able to compare the image of a face against a database of known faces for identification, utilizing the concept known as Eigenface. Specifically, the vision I have for the way this project will be implemented is to take a video stream and "scrape" faces from it, turn them into X x Y images, then into a vector (XY x 1), and then measure the Euclidean distance between that face and all others in the database. Novel vectors that are outside a certain distance from known faces/vectors (i.e. faces that are in the database) will be classified as not recognized, and vectors that are within the distance will be classified as a certain individual contained within the database. This step could likely be implemented using K-means.')
                text("")
                doc.asis('</div>')

    return doc.getvalue()


def footer():
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            with tag('form', id='menu'):
                with tag('footer'):
                    with tag('p'):
                        text("Developed for CIS4390")
                        doc.asis("<br>")
                        text(
                            "Developers: Remee A., Moise J., Luke O., Zihan S., Xinxin W.")

    return doc.getvalue()


def header():
    doc, tag, text, line = Doc().ttl()
    stylesheet = open(os.path.join(sys.path[0], "templates/stylesheet.txt"))

    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8"/>')
            with tag('title'):
                text('Oh My Py')
            with tag('style'):
                doc.asis(stylesheet.read())

    with tag('div', id='container'):
        doc.asis('<a href="'+url_for('home')+'"')
        with tag('div', id='photo-container'):
            doc.stag(
                'img', src='https://raw.githubusercontent.com/remeeliz/ohmypy/master/header.JPG', id="header")
        doc.asis('</a>')

    return doc.getvalue()


def buttons():
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button2" value="view_data" class="tooltip"> PLAY MEDIA <span class="tooltiptext">This will allow you to select a video to be played with muted commercials.</span></button>')
                doc.asis('<textarea name="content" id="hide" method="post">choose_video</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button4" value="learn_data" class="tooltip"> LEARN FACE <span class="tooltiptext">This tool is to add faces to the data set for our facial recognition program.</span></button>')
                doc.asis(
                    '<textarea name="content" id="hide" method="post">learn_face</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button5" value="database" class="tooltip"> VIEW DATA <span class="tooltiptext">This is a truncated view of the data being used for our facial recognition algorithm.</span></button>')
                doc.asis(
                    '<textarea name="content" id="hide" method="post">database</textarea>')
            with tag('form', id='menu'):
                doc.asis(
                    '<button type="submit" id="button3" value="more_info" > MORE INFO </button>')
                doc.asis(
                    '<textarea name="content" id="hide" method="post">more_info</textarea>')

    return doc.getvalue()


def choose_video():
    doc, tag, text, line = Doc().ttl()
    videolist = video_list()
    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            doc.asis('<span>Please select a media file to play. As the video plays, commercials will be muted automatically.</span></br></br>')
            with tag('form', id='menu'):
                for videoname in videolist:
                    if len(videoname) > 0:
                        doc.asis('<button type="submit" id="button2" name="video_name" value="' +
                                 videoname+'">' + videoname + '</button>')
                doc.asis(
                    '<textarea name="content" id="hide" method="post">data_page</textarea>')
    return doc.getvalue()


def video_page(videoname):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())
    doc.asis(view_data_page(videoname))
    doc.asis(footer())
    return doc.getvalue()


def view_data_page(videoname):
    doc, tag, text, line = Doc().ttl()
    with tag('div', id='photo-container'):
        doc.asis(basic_video(videoname))
    return doc.getvalue()


def learn_face():
    doc, tag, text, line = Doc().ttl()
    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            with tag('div'):
                doc.asis('<span>This page allows you to add a face to be recognized during video play back. The image vector will be added to our training set.</span></br></br>')
                doc.asis("<strong>Choose an image with a single face to train facial recognition</strong>")
                with tag('div', id='learn_face'):
                    doc.asis('<form method=post enctype=multipart/form-data>')
                    doc.asis(
                        '<label for="file-upload" class="custom-file-upload"><i class="fa fa-cloud-upload"></i>Choose File</label></br>')
                    doc.asis(
                        '<input type="file" name="file" multiple="multiple" id="file-upload" accept="image/png,image/jpeg" required></br></br>')
                    doc.asis(
                        '<input type="text" name="name_in" placeholder="Eigen Face" required>')
                    doc.asis('</br></br>')
                    doc.asis(
                        '<button type="submit" id="eval_button" value="Upload"> Evaluate </button>')
                    doc.asis('</form>')

    return doc.getvalue()


def basic_video(file_location):
    doc, tag, text, line = Doc().ttl()
    with tag('div', id='basic_vid'):
        #doc.asis('<video width="1245" height="700" id="video_player" controls><source src="static/videos/DwightBetraysMichael.mp4" type="video/mp4"></video>')
        doc.asis('<video controls id="video_player" width="1245" height="700" controls><source src="static/videos/'+file_location+'" type="video/mp4"></video>')
    return doc.getvalue()
