import requests

url = "http://disarmgis.herokuapp.com/upload"
files = {'files':open('heatvals.js','rb')}
r = requests.post(url, files=files)