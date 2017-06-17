from flask import Flask
from flask import request
from flask import request, render_template
import os, urllib, csv

app = Flask (__name__)

@app.route('/')
def table():
	file_url = 'https://raw.githubusercontent.com/Titokhan/emb_rpi_data/master/emb_data.csv'
	
	response = urllib.urlopen(file_url)
	emb_contents = list(csv.reader(response))
	
	events = len(emb_contents)

	return render_template('table.html', events=events, data_records=emb_contents)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)