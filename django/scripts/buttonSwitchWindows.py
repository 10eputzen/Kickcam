#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import time
from datetime import datetime
#from myconfig import *
from keyboard import press
import requests

code = '666'
url = 'https://firestore.googleapis.com/v1/projects/kickcam-57681/databases/(default)/documents/buttonClicks'
# GPIO 23 set up as input. It is pulled up to stop false signals
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z'
data = '''{
	"fields": {
		"time": {
			"timestampValue": "'''+timestampStr+'''"
		},
	},
}'''
def push():
	response = requests.post(url, data=data)
	print (response.content.decode('utf-8').splitlines())
	return True
#


print ("Waiting for Button Input...")
# now the program will do nothing until the signal on port 23
# starts to fall towards zero. This is why we used the pullup
# to keep the signal high and prevent a false interrupt

#print "During this waiting time, your computer is not"
#print "wasting resources by polling for a button press.\n"
#print "Press your button when ready to initiate a falling edge interrupt."
#txt = input("Type something to test this out: ")
print (data)
push()