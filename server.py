import numpy as np
import model

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

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

from flask import request

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting-result.html', greeting=greeting)

@app.route('/predict')
def predict_spam():
    return render_template('predict_spam.html')

@app.route('/predict', methods=['POST'])
def evaluate_prediction():
    guess = form.request['guess']

    predict = model.predict(guess)

    return render_template('evaluate_prediction.html', predict=predict)