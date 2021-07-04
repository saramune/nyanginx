import os

from flask import Flask,render_template

app = Flask(__name__, static_folder='images')

@app.route('/')
def hello_world():
    return render_template('index.html')
