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
    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8"/>')
            with tag('title'):
                text('Oh My Py')
            with tag('style'):
                doc.asis('body{background-color: #ffb300; font-family:"Trebuchet MS", Helvetica, sans-serif;} '
                         'h1{color: blue; font-variant: small-caps;} '
                         '#header{width: 80%; horizontal-align: center;} '
                         'div{margin: 0 auto; width: 80%; text-align: center; border-radius:6px;} '
                         'button{margin: 10px; width: 70%; height: 50px; text-align: center; box-shadow: 0px 1px 0px 0px #f0f7fa; border-radius:6px; display:inline-block; cursor:pointer; font-size:15px; font-weight:bold; text-decoration:none;} '
                         'button:hover {background:linear-gradient(to bottom, #019ad2 5%, #33bdef 100%); background-color:#019ad2;} '
                         '#button1:active,#button2:active {position:relative; top:1px;} '
                         '#button1{margin: 10px; width: 70%; height: 50px; text-align: center; box-shadow: 0px 1px 0px 0px #f0f7fa; border-radius:6px; display:inline-block; cursor:pointer; font-size:15px; font-weight:bold; text-decoration:none; color: black; line-height: 40px;} '
                         '#button1:hover{background:linear-gradient(to bottom, #019ad2 5%, #33bdef 100%); background-color:#019ad2;} '
                         '#button1:active {position:relative; top:1px;} '
                         '#button1{background:linear-gradient(to bottom, #89c403 5%, #77a809 100%); background-color:#89c403; border:1px solid #74b807;} '
                         '#button1:hover {background:linear-gradient(to bottom, #77a809 5%, #89c403 100%); background-color:#77a809;} '

                         '#button2:active,#button2:active {position:relative; top:1px;} '
                         '#button2{margin: 10px; width: 70%; height: 50px; text-align: center; box-shadow: 0px 1px 0px 0px #f0f7fa; border-radius:6px; display:inline-block; cursor:pointer; font-size:15px; font-weight:bold; text-decoration:none; color: black; line-height: 40px;} '
                         '#button2:hover{background:linear-gradient(to bottom, #019ad2 5%, #33bdef 100%); background-color:#019ad2;} '
                         '#button2:active {position:relative; top:1px;} '
                         '#button2{background:linear-gradient(to bottom, #89c403 5%, #77a809 100%); background-color:#89c403; border:1px solid #74b807;} '
                         '#button2:hover {background:linear-gradient(to bottom, #77a809 5%, #89c403 100%); background-color:#77a809;} '
                         '#button2{background:linear-gradient(to bottom, #3d94f6 5%, #1e62d0 100%); background-color:#3d94f6; border:1px solid #337fed;} '
                         '#button2:hover {background:linear-gradient(to bottom, #1e62d0 5%, #3d94f6 100%); background-color:#1e62d0;} '

                         '#button3{background:linear-gradient(to bottom, #ffec64 5%, #ffab23 100%); background-color:#ffec64; border:1px solid #ffaa22;} '
                         '#button3:hover {background:linear-gradient(to bottom, #ffab23 5%, #ffec64 100%); background-color:#ffab23;} '
                         '#button3:active + #more_info {display: block;} '

                         '#test{display: none;} '
                         '#hide{display: none;} '
                         'a { text-decoration: none; color: black;} '

                         '#more_info{display: none;}'

                         '#display_info{font-size:10px; font-weight:normal; text-align: justify;} '
                         '#return_image{width: 50%;} '
                         '#display_face{font-size:10px; font-weight:normal; text-align: justify; background-color: #e0e0e0; padding: 10px 10px; width: 50%; } '
                         
                         '#learn_face{font-size:10px; font-weight:normal; text-align: center;padding: 25px 50px;background-color: #e0e0e0; margin-top: 10px;}'
                         '.custom-file-upload {border: 1px solid #ccc; display: inline-block; padding: 6px 12px; cursor: pointer;} '
                         '#eval_button{margin: 10px; width: 50%; height: 5%; text-align: center; box-shadow: 0px 1px 0px 0px #f0f7fa; border-radius:6px; cursor:pointer; font-size:15px; font-weight:bold; text-decoration:none;} '
                         
                         'input[type="file"] {display: none;} '
                         '.alert {  padding: 20px;  background-color: #f44336;  color: white;} .closebtn {  margin-left: 15px;  color: white;  font-weight: bold;  float: right;  font-size: 22px;  line-height: 20px;  cursor: pointer;  transition: 0.3s;} .closebtn:hover {  color: black;}'
                         'footer{font-size:8px; font-weight:bold; text-align: center; position: fixed; left:0; bottom:0; width: 100%}'
                         '')

    with tag('div', id='container'):
        doc.asis('<a href="."')
        with tag('div', id='photo-container'):
            doc.stag('img', src='https://raw.githubusercontent.com/remeeliz/ohmypy/master/header.JPG', id="header")
        doc.asis('</a>')

    return doc.getvalue()

def buttons():
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            with tag('form', id='menu'):
                doc.asis('<label id="button1" for="test" > SELECT MEDIA FILE </label><br>')
                doc.asis('<input type="file" id="test" accept="image/png, image/jpeg, video/mp4">')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button2" value="view_data"> VIEW DATA </button>')
                doc.asis('<textarea name="content" id="hide" method="post">view_data</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button4" value="learn_data"> LEARN FACE </button>')
                doc.asis('<textarea name="content" id="hide" method="post">learn_face</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button3" value="more_info"> MORE INFO </button>')
                doc.asis('<textarea name="content" id="hide" method="post">more_info</textarea>')

    return doc.getvalue()

def view_data_page():    
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='photo-container'):
        doc.stag('img', src=url_for('video_feed'), klass="photo")
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