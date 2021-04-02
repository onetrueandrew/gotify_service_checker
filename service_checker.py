#!/usr/bin/env python

import urllib.request
import requests
import sys,os

# USER CONFIGS:
file1 = open(os.path.join(sys.path[0], "services.conf.py"),'r')
gotify_token = 'EXAMPLE_KEY'
gotify_api = 'http://10.0.0.2:8050/message'
# END USER CONFIG

Lines = file1.readlines()
params = (
    ('token', gotify_token),
)

for line in Lines:
	if line.startswith("#"):
		pass
	else:
		service = line.split(' ')[0]
		location = line.split(' ')[1]
		gotify_priority = line[-2]
		files = {'title': (None, service),'message': (None, 'Service detected down'),'priority': (None, gotify_priority),}
		try:
			code = (urllib.request.urlopen(location).getcode())
			if code == 200:
				#print(service + ' works!')
				pass
			else:
				response = requests.post(gotify_api, params=params, files=files)
		except:
			response = requests.post(gotify_api, params=params, files=files)
