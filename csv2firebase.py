# -*- coding: utf-8 -*-

import csv
import json
from firebase import firebase
import datetime
#mi objeto de firebase
firebase = firebase.FirebaseApplication('https://haha-4cf04.firebaseio.com', None)
     
data = []

#LEYENDO INFO DEL CSV 
with open('/home/hridoy/Downloads/emb_data.csv') as csvfile:
	read = csv.reader(csvfile)
	for row in read:#leyendo todas las filas
		date = str(row[0])
		time = str(row[1])
		serial = int(row[2])	
		pm10 = float(row[3])
		pm2 = float(row[4])
		pm1 = float(row[5])
		no2 = float(row[6])
		co2 = float(row[7])
		co = float(row[8])
		humidity = float(row[9])
		temp = float(row[10])
		dateTime1 = date + time
		#dateTime = datetime.datetime.strptime(dateTime, "%Y/%m/%d %H:%M:%S")
		dateTime = int((datetime.datetime.strptime(dateTime1, "%Y/%m/%d %H:%M:%S")+ datetime.timedelta(days=17,hours=15,minutes=35)).strftime('%s')) * 1000
		dateTime = dateTime  
		#print str(dateTime1) + '->' + str(dateTime)
		
		firebase.put('/sensors',serial,{"DateTime": dateTime,"pm10": pm10,"pm2": pm2,"pm1": pm1,"no2": no2,"co2": co2,"co": co,"temp": temp,"humid": humidity})
		