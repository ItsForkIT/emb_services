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

	emb2 = []
	for rows in xrange(1,events-1):
		emb2.append(emb_contents[rows])
		
	events = len(emb_contents)

	return render_template('table.html', events=events-2, data_records=emb2)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)