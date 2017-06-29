from flask import Flask
from flask import request
from flask import request, render_template
app = Flask (__name__)

@app.route('/')
def table():
	return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)