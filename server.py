import numpy as np

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/hello/<name>')
def sayhello(name):
    return f"Hi {name}, How are you doing today?"

@app.route('/roll-dice')
def roll_dice():
    rand =  np.random.randint(1, 6, 3)
    x = rand[0].astype(str)
    y = rand[1].astype(str)
    z = rand[2].astype(str)
    return f'The three random numbers are {x}, {y} and {z}'
