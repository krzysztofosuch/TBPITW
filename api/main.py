from flask import Flask
from params import *

app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello, World!'

@app.route('/singleRead')
def singleRead():
        return Params().singleRead()

@app.route('/singleSteadyRead')
def singleSteadyRead():
        return Params().singleSteadyRead()

@app.route('/readUart')
def readUart():
        return Params().readUart()

@app.route('/dron')
def dron():
        return Params().restartDron()

