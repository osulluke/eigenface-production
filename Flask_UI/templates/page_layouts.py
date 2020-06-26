from yattag import Doc
from flask import url_for

def get_page(page_name):
    doc, tag, text, line = Doc().ttl()
    with tag('html'):
        with tag('head'):
            with tag('title'):
                text('Oh My Py')
            with tag('style'):
                doc.asis('body{background-color: #ffb300; font-family:"Trebuchet MS", Helvetica, sans-serif;} '
                         'h1{color: blue; font-variant: small-caps;} '
                         '#header{width: 80%; horizontal-align: center;} '
                         'div{margin: 0 auto; width: 80%; text-align: center;} '
                         'button{margin: 10px; width: 70%; height: 50px; text-align: center; box-shadow: 0px 1px 0px 0px #f0f7fa; border-radius:6px; display:inline-block; cursor:pointer; font-size:15px; font-weight:bold; text-decoration:none;} '
                         'button:hover {background:linear-gradient(to bottom, #019ad2 5%, #33bdef 100%); background-color:#019ad2;} '
                         '#button1:active,#button2:active {position:relative; top:1px;} '
                         '#button1{margin: 10px; width: 70%; height: 50px; text-align: center; box-shadow: 0px 1px 0px 0px #f0f7fa; border-radius:6px; display:inline-block; cursor:pointer; font-size:15px; font-weight:bold; text-decoration:none; color: black; line-height: 40px;} '
                         '#button1:hover{background:linear-gradient(to bottom, #019ad2 5%, #33bdef 100%); background-color:#019ad2;} '
                         '#button1:active {position:relative; top:1px;} '
                         '#button1{background:linear-gradient(to bottom, #89c403 5%, #77a809 100%); background-color:#89c403; border:1px solid #74b807;} '
                         '#button1:hover {background:linear-gradient(to bottom, #77a809 5%, #89c403 100%); background-color:#77a809;} '
                         '#button2{background:linear-gradient(to bottom, #3d94f6 5%, #1e62d0 100%); background-color:#3d94f6; border:1px solid #337fed;} '
                         '#button2:hover {background:linear-gradient(to bottom, #1e62d0 5%, #3d94f6 100%); background-color:#1e62d0;} '
                         '#button2:active '
                         '#button3{background:linear-gradient(to bottom, #ffec64 5%, #ffab23 100%); background-color:#ffec64; border:1px solid #ffaa22;} '
                         '#button3:hover {background:linear-gradient(to bottom, #ffab23 5%, #ffec64 100%); background-color:#ffab23;} '                         
                         '#test{display: none;} '
                         '#hide{display: none;} '
                         '#more_info{display: none;}'
                         'footer{font-size:8px; font-weight:bold; text-align: center; position: fixed; left:0; bottom:0; width: 100%}'
                         '#display_info{font-size:10px; font-weight:normal; text-align: justify;}'
                         '#button3:active + #more_info {display: block;} '
                         '')
    
    
    if page_name == "data_page":
        doc.asis(home_page())
        doc.asis(view_data_page())
    elif page_name == "more_info":
        doc.asis(home_page())
        doc.asis(buttons())
        doc.asis(info_page())
    else:
        doc.asis(home_page())
        doc.asis(buttons())        

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

def home_page():
    doc, tag, text, line = Doc().ttl()
    with tag('html'):
        with tag('head'):
            with tag('title'):
                text('Oh My Py')
            with tag('style'):
                doc.asis('body{background-color: #ffb300; font-family:"Trebuchet MS", Helvetica, sans-serif;} '
                         'h1{color: blue; font-variant: small-caps;} '
                         '#header{width: 80%; horizontal-align: center;} '
                         'div{margin: 0 auto; width: 80%; text-align: center;} '
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
                         '#test{display: none;} '
                         '#hide{display: none;} '
                         'a { text-decoration: none; color: black;} '
                         '#more_info{display: none;}'
                         '#display_info{font-size:10px; font-weight:normal; text-align: justify;}'
                         '#button3:active + #more_info {display: block;} '
                         '.alert {  padding: 20px;  background-color: #f44336;  color: white;} .closebtn {  margin-left: 15px;  color: white;  font-weight: bold;  float: right;  font-size: 22px;  line-height: 20px;  cursor: pointer;  transition: 0.3s;} .closebtn:hover {  color: black;}'
                         '')

    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            doc.stag('img', src='https://raw.githubusercontent.com/remeeliz/ohmypy/master/header.JPG', id="header")

    return doc.getvalue()

def buttons():
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            with tag('form', id='menu'):
                doc.asis('<label id="button1" for="test" > SELECT MEDIA FILE </label><br>')
                doc.asis('<input type="file" id="test" accept="image/png, image/jpeg, video/mp4">')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button2" value="view_dat"> VIEW DATA </button>')
                doc.asis('<textarea name="content" id="hide" method="post">view_data</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button3" value="more_info"> MORE INFO </button>')
                doc.asis('<textarea name="content" id="hide" method="post">more_info</textarea>')

    return doc.getvalue()

def view_data_page():    
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='photo-container'):
        doc.stag('img', src=url_for('video_feed'), klass="photo")
    return doc.getvalue()