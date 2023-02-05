import os
import random

import flask
from flask import Flask, redirect, session
from flask import request
from flask_session import Session
from flask import render_template
from waitress import serve
import gym

app = Flask(__name__)
app.secret_key = 'the awesome super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)

count = 0

@app.route('/')
def render_main():
    return render_template('home.html')

#For cardio choices
@app.route('/chosenof',methods=['GET', 'POST'])
def chosen():
    cardio=[{'car': 'Bike'}, {'car': 'Run'}, {'car':'Walk and Sprint'}]

    return render_template('chosenof.html', cardiochoices=random.sample(cardio,2))

#For choices of strength-training
@app.route('/chosenof2',methods=['GET', 'POST'])
def chosen2():
    weight=[{'strength': 'Pushups'}, {'strength': 'Situps'}, {'strength': 'Curl Ups'}, {'strength': 'Squats'}, {'strength': 'Lunges'}, {'strength': 'Russian Twists'}, {'strength': 'High-knees'}, {'strength': 'Side-lunges'}, {'strength': 'V-ups'}, {'strength': 'Jumping jacks'}, {'strength': 'Superman'}, {'strength': 'Bicycle'}, {'strength': 'Vertical Crunch'}, {'strength': 'Spiderman plank'}, {'strength': 'Bird dog'}, {'strength': 'Tuck jump'}, {'strength': 'Mountain climbers'}, {'strength': 'Bridge'}, {'strength': 'Floor dips'}, {'strength': 'Ski jumper'}, {'strength': 'Dragon walk'}, {'strength': 'Reverse crunch'}, {'strength': '1 leg bridge'}, {'strength': 'Bear hug'}, {'strength': '180 Squat Jump'}, {'strength': 'Squat Jump'}, {'strength': 'Cross toe touch'}, {'strength': 'Plank reach'}, {'strength': 'Inchworm'}, {'strength': 'Pike up'}, {'strength': 'Lateral Jump'}, {'strength': 'Scissor jump'}, {'strength': 'Jackknives'}]
    return render_template('/chosenof2.html', weightchoices=random.sample(weight,8))

#For the time choices
@app.route('/time',methods=['GET', 'POST'])
def chosen3():
    amount = [{'t': 5}, {'t': 7}, {'t': 10}, {'t': 12}, {'t': 15}, {'t': 20}, {'t': 25}, {'t': 30}, {'t': 35},
              {'t': 40}, {'t': 45}, {'t': 50}, {'t': 55}, {'t': 60}]
    return render_template('/time.html', timechoices=random.sample(amount,4))

#displays everything at the end
@app.route('/chosenofresult', methods=['GET', 'POST'])
def chosenofresult():
    if request.form.get('chosen1'):
        temp1 = str(request.form.get('chosen1'))
        session['chosen1'] = temp1
        return redirect('/time')
    if request.form.get('chosen3'):
        temp3 = str(request.form.get('chosen3'))
        session['chosen3'] = temp3
        return redirect('/chosenof2')
    if request.form.get('chosen2'):
        temp1 = session.get('chosen1')
        temp3 = session.get('chosen3')
        temp2 = request.form.getlist('chosen2')
        temp2 = ', '.join(temp2)
        return render_template('chosenofresult.html',select1=temp1, select2=temp2, select3=temp3)


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8000))
    serve(gym.app, host='127.0.0.1', port=8000,url_prefix="/gymApp",url_scheme='https')
    with app.test_request_context("/"):
        session["key"] = "value"

