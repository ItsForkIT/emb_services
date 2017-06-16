import os
import sys

dirName = sys.argv[1]
heatvals = ""
allFilesList = os.listdir(dirName)

for files in allFilesList:
	if files[0:3] == 'SMS':
		splitFile = files.split("_")
		with open(os.path.join(dirName,files), 'r') as smsFile:
			data=smsFile.read()
		heatvals = heatvals + "[" + str(splitFile[5])  + ',' + splitFile[6] +',"' + splitFile[2] +'","' + data +'","' + splitFile[3] + "\"],"
		print heatvals

heatstr = '''var addressPoints = [
%s
];''' % heatvals

with open('heatvals.js', 'w') as f:
	f.write(heatstr)
		
