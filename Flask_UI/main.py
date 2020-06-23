from flask import Flask, render_template, request
from templates import *
from database import *
from media_player import *
from webstreaming import *

app = Flask(__name__)

@app.route("/")
def home():
    url_get = request.args.get('content')
    #zihan - set video variable
    if url_get == 'set_video':
        return get_page(url_get)
    if url_get == 'more_info':
        return get_page(url_get)
    if url_get == 'view_data':
        return get_page('data_page')
    else:
        return get_page('')

if __name__ == "__main__":
    app.run(debug=True)

