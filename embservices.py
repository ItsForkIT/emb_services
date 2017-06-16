from flask import Flask
from flask import request
from flask import request, render_template
import os, urllib, csv

app = Flask (__name__)

@app.route('/')
def table():
	file_url = 'https://gist.githubusercontent.com/hridaydutta123/f666b6990d5b00c2a862445230e4816c/raw/ef4d334845ebeb3d77cc09bfe87c65160df8b738/gistfile1.txt'
	
	response = urllib.urlopen(file_url)
	emb_contents = list(csv.reader(response))
	events = len(emb_contents)
    
	minTime = emb_contents[0][1]
	maxTime = emb_contents[events-1][1]
	print minTime
	print maxTime

	return render_template('table.html', events=events, data_records=emb_contents)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)