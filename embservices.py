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

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)