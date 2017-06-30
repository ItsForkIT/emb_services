import json
from time import time
from firebase import firebase
from random import random
from flask import Flask, render_template, make_response

app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://haha-4cf04.firebaseio.com', None)

@app.route('/')
def hello_world():
	return render_template('index.html', data='test')

@app.route('/live-data')
def live_data():
	# Create a PHP array and echo it as JSON
	result = firebase.get('/scores',None)
	for i in result:
		data1=result[i].pm10
		data = [time() * 1000, data1]
		response = make_response(json.dumps(data))
		response.content_type = 'application/json'
		return response

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=5000)
