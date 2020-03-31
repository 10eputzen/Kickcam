#!/usr/bin/python
 # Purges all ELMAH log files older than 7 days and all tempfiles older than 3 days.
import os, time, datetime
today = datetime.datetime.now().date()
todayString = str(today)
def purgeDir(dir, age):
	print "Scanning:", dir
	for f in os.listdir(dir):

		now = time.time()
		filepath = os.path.join(dir, f)
		modified = os.stat(filepath).st_mtime
		if modified < now - age: 
			if os.path.isfile(filepath):
				os.remove(filepath)
				print 'Deleted: %s (%s)' % (f, modified)

# 2 Hours	= 7200 seconds
folderPath = "/opt/KickCam/KickCam/html/video/"+todayString
if os.path.isdir(folderPath) is True:
	purgeDir(folderPath,(7200))
