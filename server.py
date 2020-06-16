import numpy as np

from flask import Flask

app = Flask(__name__)

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/')
# def index():
#     return 'Hello, World!'

@app.route('/hello/<name>')
def sayhello(name):
    return f"Hi {name}, How are you doing today?"

@app.route('/roll-dice')
def roll_dice():
    rand =  np.random.randint(1, 6, 3)
    x = rand[0].astype(str)
    y = rand[1].astype(str)
    z = rand[2].astype(str)
    return render_template('roll-dice.html', x=x, y=y, z=z)
