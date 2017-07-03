from flask import Flask
from firebase import firebase
from flask import request
from flask import request, render_template
app = Flask (__name__)

firebase = firebase.FirebaseApplication('https://haha-4cf04.firebaseio.com', None)
result1 = firebase.get('/scores',None)
@app.route('/')
def table():
	result = firebase.get('/scores', None)
  	return render_template('index.html', messages=result)

@app.route('/graph')
def graph():
	data1=[]
	result="CO&CO2"
	result1 = firebase.get('/scores',None)
	for i in result1:
		data1.append(float(result1[i]['serial']))
	print len(data1)
	return render_template('graph.html', name1=result, messages=data1)

@app.route('/graph1')
def graph1():
	data1=[]
	data2=[]
	data3=[]
	data4=[]
	result="PM Graph"
	for i in result1:
		data1.append(int(result1[i]['pm2'].replace(' ','')))
	for i in result1:
		data2.append(int(result1[i]['pm10'].replace(' ','')))
	for i in result1:
		data3.append(int(result1[i]['pm1'].replace(' ','')))
	for i in result1:
		data4.append(str(result1[i]['time'].replace(' ','')))
	print data2
	return render_template('graph.html', name1=result, messages=data1,messages1=data2,messages2=data3,messages3=data4,n1="PM2.5",n2="PM10",n3="PM1")

@app.route('/graph2')
def graph2():
	result="T  H Graph"
	data1=[]
	data2=[]
	for i in result1:
		data1.append(float(result1[i]['temp'].replace(' ','')))
	for i in result1:
		data2.append(float(result1[i]['humidity'].replace(' ','')))
	print data2
	return render_template('graph.html', name1=result, messages=data1,messages1=data2,n1="Temperature",n2="Humidity")

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')