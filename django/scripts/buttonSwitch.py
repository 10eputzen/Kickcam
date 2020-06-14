#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
import time
import urllib2
from datetime import datetime
#from myconfig import *
import requests
GPIO.setmode(GPIO.BCM)

code = '666'
url = 'https://firestore.googleapis.com/v1/projects/kickcam-57681/databases/(default)/documents/buttonClicks'
# GPIO 23 set up as input. It is pulled up to stop false signals
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
def push(message):
	data = '''{
      "fields": {
        "time": {
          "timestampValue":'''+ timestampStr +'''
        },
      },
	}'''
	response = requests.post(url, data=data)
	print (response)
	return True
#

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print ("Waiting for Button Input...")
# now the program will do nothing until the signal on port 23
# starts to fall towards zero. This is why we used the pullup
# to keep the signal high and prevent a false interrupt

#print "During this waiting time, your computer is not"
#print "wasting resources by polling for a button press.\n"
#print "Press your button when ready to initiate a falling edge interrupt."
while True:
	try:
		GPIO.wait_for_edge(23, GPIO.RISING)
		print ("\nButton Press detected. Firing POST Call to:\n")
		print(url)
		push(url)
		time.sleep(0.3)
	except KeyboardInterrupt:
	        GPIO.cleanup()       # clean up GPIO on CTRL+C exit
	#GPIO.cleanup()           # clean up GPIO on normal exit

