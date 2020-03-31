#For Python 3 use urllib.request
#import urllib.request, urllib.parse, urllib.error
import urllib2
import subprocess, os
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.http import HttpResponse



def StartConversion(request, *args, **kwargs):   
	downloadUrl = 'http://192.168.178.138/video/currentReplay/mylist.txt'
	getFile(downloadUrl)
	convertVideo('1','benny')
	return HttpResponse("1")

def getFile(link):
    f = urllib2.urlopen(link)
    with open('mylist.txt','wb') as output:
      output.write(f.read())


def convertVideo(frames,audio): 
    audioPath = '../html/audio/'+audio+'.mp3'
    currentReplayPath = '../html/video/currentReplay/'
    replayName = 'currentReplay'
    #speed = '2'
    speed = frames
    
    subprocess.call(
    #'ffmpeg -i '+path+replayName+'.avi -acodec libfaac -b:a 128k -vcodec mpeg4 -filter:v "setpts=2.0*PTS" -pix_fmt yuv420p  -y -b:v 1200k -flags +aic+mv4 '+path+outputName+'.mp4',
    #'ffmpeg '+videos +' -i '+audioPath+' -c:v libx264 -filter:v "setpts='+speed+'*PTS" -y -c:a aac \
    'ffmpeg -f concat -safe 0 -protocol_whitelist "file,http,https,tcp,tls" -i mylist.txt -i '+audioPath+' -c:v libx264 -filter:v "setpts='+speed+'*PTS" -y -c:a aac \
    -movflags +faststart -shortest '+currentReplayPath+replayName+'.mp4',shell=True)

    cmd = 'cat %(jpegs)s | ffmpeg -framerate %(framerate)s -f image2pipe -vcodec mjpeg -i - -vcodec mpeg4 -b:v %(bitrate)s -qscale:v 0.1 -f avi %(tmp_filename)s'


urlpatterns = [
    url(r'^start/$', StartConversion),
	url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
urlpatterns = format_suffix_patterns(urlpatterns)

