from flask import Flask
from firebase import firebase
from flask import request
from flask import request, render_template
app = Flask (__name__)

firebase = firebase.FirebaseApplication('https://haha-4cf04.firebaseio.com', None)

@app.route('/')
def table():
	result = firebase.get('/scores', None)
  	return render_template('index.html', messages=result)

@app.route('/graph')
def graph():
	result="CO&CO2"
	data = firebase.get('/scores', None)
	return render_template('graph.html', name1=result, messages=data)

@app.route('/graph1')
def graph1():
	result="PM Graph"
	return render_template('graph.html', name1=result, messages=data)

@app.route('/graph2')
def graph2():
	result="T&H Graph"
	return render_template('graph.html', name1=result, messages=data)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')