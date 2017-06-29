from flask import Flask
from flask import request
from flask import request, render_template
import os, urllib, csv

app = Flask (__name__)

@app.route('/')
def table():
	file_url = 'https://raw.githubusercontent.com/Titokhan/emb_rpi_data_test/master/emb_data.csv'

	response = urllib.urlopen(file_url)
	emb_contents = list(csv.reader(response))
	events = len(emb_contents)

	emb2 = []
	for rows in xrange(2,events-1):
		if rows % 5 == 0:
		 	emb2.append(emb_contents[rows])

	emb_len = len(emb2)
	return render_template('table.html', events=emb_len, data_records=emb2)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)