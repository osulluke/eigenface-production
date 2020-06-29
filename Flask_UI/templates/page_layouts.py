##################################################
## FileName: page_layouts.py
##################################################
## Author: RDinmore
## Date: 2020.06.22
## Purpose: return html to be displayed
## Libs: yattag, flask, urllib
## Path: Flask_UI/templates
##################################################

from yattag import Doc
from flask import url_for
import urllib.parse
import os
import sys
import pandas as pd

def get_page(page_name):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())

    if page_name == "data_page":
        doc.asis(view_data_page())
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
    html = datatable.to_html()
    doc.asis(html)
    doc.asis(footer())
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
            text("Name: " +  urllib.parse.unquote_plus(image_name))
            doc.asis('</br>')
            text("Face count: " + str(output_count))
            doc.asis('</br>')
            doc.asis('</br>')
    doc.asis(footer())
    return doc.getvalue()

def info_page():
    doc, tag, text, line = Doc().ttl()
    with tag('div'):
        with tag('div', id='container'):
            with tag('div', id='display_info'):
                doc.asis('<div class="alert"><span class="closebtn" onclick="this.parentElement.style.display='+"'none'"+';">x</span>')
                text("This is a facial recognition media player. After selecting a media file the software will parse facial images and insert them into the database. ")
                text("These images will then be compared to current images and highlighted if recognized. The images will also be used to continue to grow the facial ")
                text("recognition data set.")
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
                        text("Developers: Remee A., Martin L., Luke O., Zihan S., Xinxin W.")

    return doc.getvalue()

def header():
    doc, tag, text, line = Doc().ttl()
    stylesheet = open(os.path.join(sys.path[0],"templates/stylesheet.txt"))

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
            doc.stag('img', src='https://raw.githubusercontent.com/remeeliz/ohmypy/master/header.JPG', id="header")
        doc.asis('</a>')

    return doc.getvalue()

def buttons():
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            with tag('form', id='menu'):
                doc.asis('<label id="button1" for="test" > SELECT YOUR MEDIA FILE </label><br>')
                doc.asis('<input type="file" id="test" accept="image/png, image/jpeg, video/mp4">')
            with tag('form', id='menu'):
                doc.asis('<label id="checkboxlabel" for="mute" > MUTE COMMERCIALS </label>')
                doc.asis('<input type="checkbox" id="mute" name="mute" value="Mute"></br></br>')
                doc.asis('<button type="submit" id="button2" class="tooltip" value="view_data"> PLAY MEDIA <span class="tooltiptext">The page will allow you to select media files (formatted as .mp4) that have been provided from some source, currently, these are part of the repo itself, and are limited to short clips of the television show "The Office." It is not necessary for the user to provide a novel file.</span></button>')
                doc.asis('<textarea name="content" id="hide" method="post">data_page</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button4" value="learn_data" class="tooltip"> LEARN FACE <span class="tooltiptext">This page will then allow you to play that file using our technique that will scrape images of faces detected in the video stream, and identify them as a known character (actor) in the stream. Prior to playing the stream, the user can select what they would like to have happen when known faces are identified in the stream (i.e. mute, change the channel, etc.).</br></br>Currently, this function is limited to finding faces in the stream; identifying them has not yet been implemented. You can see, however, that as the stream is played, the face that is detected in the stream is identified and marked by a green square.</span></button>')
                doc.asis('<textarea name="content" id="hide" method="post">learn_face</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button5" value="database"> VIEW DATA </button>')
                doc.asis('<textarea name="content" id="hide" method="post">database</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button3" value="more_info"> MORE INFO </button>')
                doc.asis('<textarea name="content" id="hide" method="post">more_info</textarea>')

    return doc.getvalue()

def view_data_page():    
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='photo-container'):
        doc.asis('<iframe width="1000" height="500" src="'+url_for('video_feed')+'" frameborder="0" allowfullscreen></iframe>')
    return doc.getvalue()

def learn_face():
    doc, tag, text, line = Doc().ttl()
    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            with tag('div'):
                text("Choose an image with a single face to train facial recognition")
                with tag('div', id='learn_face'):
                    doc.asis('<form method=post enctype=multipart/form-data>')
                    doc.asis('<label for="file-upload" class="custom-file-upload"><i class="fa fa-cloud-upload"></i>Choose File</label></br>')
                    doc.asis('<input type="file" name="file" id="file-upload" accept="image/png,image/jpeg" required></br></br>')
                    doc.asis('<input type="text" name="name_in" placeholder="Eigen Face" required>')
                    doc.asis('</br></br>')
                    doc.asis('<button type="submit" id="eval_button" value="Upload"> Evaluate </button>')
                    doc.asis('</form>')

    return doc.getvalue()