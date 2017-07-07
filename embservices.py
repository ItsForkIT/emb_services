from flask import Flask
from firebase import firebase
from flask import request
from flask import request, render_template
import json
from HTMLParser import HTMLParser

app = Flask (__name__)

firebase = firebase.FirebaseApplication('https://haha-4cf04.firebaseio.com', None)
result = firebase.get('/sensors',None)

@app.route('/real')
def real():
	result = firebase.get('/sensors',None)
	name = "RealTime Graph"
	pm2Data = []
	dateTime = []
	for values in range(1,len(result)):
		pm2Data.append(result[values]['DateTime'])
		dateTime.append(result[values]['pm2'])
	unit="asd"
	return render_template('index.html', messages=zip(pm2Data,dateTime), name=name, unit=unit)

@app.route('/graph')
def graph():
	co = []
	co2 = [] 
	dateTime = [] 
	dataOf ="CO-CO2 Graph"
	unit = HTMLParser().unescape('&micro;g/m')
	result1 = firebase.get('/sensors',None)

	for values in range(1,len(result1)):
		co.append(result1[values]['co'])
		co2.append(result1[values]['co2'])
		dateTime.append(result1[values]['DateTime'])

	return render_template('graph.html', name=dataOf, co=zip(dateTime, co), co2=zip(dateTime, co2), unit=unit, n1="CO", n2="CO2")

@app.route('/graph1')
def graph1():
	pm1 = []
	pm2 = []
	pm10 = []
	time = []
	dataOf="PM Graph"
	result1 = firebase.get('/sensors',None)
	
	for values in range(1,len(result1)):
		pm1.append(result1[values]['pm1'])
		pm2.append(result1[values]['pm2'])
		pm10.append(result1[values]['pm10'])
		time.append(result1[values]['DateTime'])

	return render_template('graph.html', name=dataOf, pm1=zip(time,pm1),pm2=zip(time,pm2),pm10=zip(time,pm10),n1="PM2.5",n2="PM10",n3="PM1")

@app.route('/graph2')
def graph2():
	dataOf = "Temperature-Humidity Graph"
	temp = []
	humid = []
	time = []
	result1 = firebase.get('/sensors',None)
	for values in range(1,len(result1)):
		temp.append(result1[values]['temp'])
		humid.append(result1[values]['humid'])
		time.append(result1[values]['DateTime'])
		
	return render_template('graph.html', name=dataOf, temp=zip(time,temp), humid=zip(time,humid), n1="Temperature", n2="Humidity")

@app.route('/')
def dashboard():
	return render_template('dashboard.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')