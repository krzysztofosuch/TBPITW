from flask import Flask
from params import *

app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello, World!'

@app.route('/singleRead')
def singleRead():
        Params().singleRead()

