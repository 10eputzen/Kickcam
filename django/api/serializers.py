from pprint import pprint
from rest_framework import serializers
from api.models import Replay, Features, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
import os
from findtools.find_files import (find_files, Match)
from os.path import basename
import subprocess, os
from datetime import datetime
import datetime
from bisect import bisect_left
import io
import time
import shutil
from subprocess import Popen
import urllib2

videoFolder = '../html/video/'
currentReplayPath = '../html/video/currentReplay/'
pathToVideoList = '../html/video/currentReplay/mylist.txt'
replayName = 'currentReplay'
sourceVideoFormat = '.avi'
pathToArchiveFolder = '../html/video/archive/'
restUrl = 'http://192.168.178.116:8001/start/'

class ReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        fields = ('pk', 'audio','duration','frames','date','filePath')


    def create(self, validated_data):
        """
        Create and return a new `Activity` instance, given the validated data.
        """
        

        start_time = time.time()   

        #Use Avi Videos 
        #Check if FFMPEG is running
        filename = '';
        pid = subprocess.call(['pgrep ffmpeg'], shell=True)
        if(pid == 1) is True:
            filename = getFilenamesFromFolder(validated_data)
            validated_data['filePath'] = filename          
            #rest_get(restUrl)
        #Use H.264 Videos
        #recordVideo(validated_data)
        else: 
            print("A Replay is already been converted")
        print("---Duration:  %s seconds ---" % round((time.time() - start_time),2))
        return Replay.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Activity` instance, given the validated data.
        """
        # instance.audio = validated_data.get('audio', instance.audio) 
        # instance.duration = validated_data.get('duration', instance.duration)    
        # instance.frames = validated_data.get('frames', instance.frames)    
        # instance.date = validated_data.get('date', instance.date)    
        # instance.filePath = validated_data.get('filePath', instance.filePath)    
        filePath = validated_data.get('filePath', instance.filePath)
        archiveReplay(filePath)


        #instance.save()
        return instance


def rest_get(message):
    url_response = urllib2.urlopen(message)
    return True

def recordVideo(data):
    #duration = data['duration']
    duration = 5
    print('Stop Recording')
    subprocess.call(['pkill raspivid'], shell=True)
    print('Convert to Mp4')
    subprocess.call(['MP4Box -add '+currentReplayPath+'currentReplay.h264 '+currentReplayPath+'currentReplay_long.mp4'], shell=True)
    print('Shorten Video')
    subprocess.call(['ffmpeg -y -sseof -'+str(duration)+' -i '+currentReplayPath+'currentReplay_long.mp4 -c copy '+currentReplayPath+'currentReplay.mp4'], shell=True)

    process = subprocess.Popen('raspivid -o '+currentReplayPath+'currentReplay.h264 -t 600000 -w 1280 -h 720', stdout=subprocess.PIPE, shell=True)
    #pkill raspivid

def archiveReplay(filePath):
    today = datetime.datetime.now().date()
    todayString = str(today)

    srcfile = currentReplayPath+replayName+'.mp4'
    dstroot = pathToArchiveFolder+todayString


    assert not os.path.isabs(srcfile)
    #dstdir =  os.path.join(dstroot, os.path.dirname(srcfile))
    #print(dstdir)
    os.makedirs(dstroot, exist_ok=True)
    shutil.copy(srcfile, dstroot)
    os.rename(dstroot+'/'+replayName+'.mp4', dstroot+'/'+filePath+'.mp4')

def getFilenamesFromFolder(data): #program does nothing as written
    #print repr(data).decode("unicode-escape")
    audio = data['audio']
    duration = data['duration']
    frames = str(data['frames'])
    date = data['date']

    found_file = 'empty';
    res = 'Error'
    # Recursively find all *.sh files in **/usr/bin**


    today = datetime.datetime.now().date()
    todayString = str(today)
    now = date.time()
    #pathToVideoFolder = '../'+todayString+'/' 
    pathToVideoFolder = 'http://192.168.178.138/video/'+todayString+'/' 
    minutes = now.minute
    sh_files_pattern = Match(filetype='f', name='*'+sourceVideoFormat)
    try:
        #found_files = find_files(path='../html/video/'+todayString, match=sh_files_pattern)
        found_files = find_files(path=videoFolder+todayString, match=sh_files_pattern)

        listOfName = []
        shortList = []


        for found_file in found_files:
            fileNames = basename(found_file).replace(sourceVideoFormat,"")
            listOfName.append(fileNames)
            #emptyList.append(fileNames)

        #listOfName = list(reversed(listOfName))
        if listOfName:
            listOfName = sorted(listOfName, key=lambda x: datetime.datetime.strptime(x, '%H-%M-%S'))
            listOfName = list(reversed(listOfName))
            print (listOfName)
            for x in range(duration, 0,-1):      
                shortList.append(listOfName[x])  
                res = listOfName[x]   
            WriteToTextfile2(pathToVideoFolder, shortList);
            #convertVideo(frames, audio)
        else:
            print("List is empty")
            res = found_file
    except Exception as e:
        print(e)
    return res




def convertVideo(frames,audio): 
    audioPath = '../html/audio/'+audio+'.mp3'
    #currentReplayPath = '../html/video/currentReplay/'
    #speed = '2'
    speed = frames
    
    subprocess.call(
    #'ffmpeg -i '+path+replayName+'.avi -acodec libfaac -b:a 128k -vcodec mpeg4 -filter:v "setpts=2.0*PTS" -pix_fmt yuv420p  -y -b:v 1200k -flags +aic+mv4 '+path+outputName+'.mp4',
    #'ffmpeg '+videos +' -i '+audioPath+' -c:v libx264 -filter:v "setpts='+speed+'*PTS" -y -c:a aac \
    'ffmpeg -f concat -safe 0 -i '+currentReplayPath+'mylist.txt -i '+audioPath+' -c:v libx264 -filter:v "setpts='+speed+'*PTS" -y -c:a aac \
    -movflags +faststart -shortest '+currentReplayPath+replayName+'.mp4',shell=True)

    cmd = 'cat %(jpegs)s | ffmpeg -framerate %(framerate)s -f image2pipe -vcodec mjpeg -i - -vcodec mpeg4 -b:v %(bitrate)s -qscale:v 0.1 -f avi %(tmp_filename)s'


def WriteToTextfile(path,text):
    pathToVideoFolder = path

    file = open(pathToVideoList, 'w')

    for lines in text:
        file.write('file \''+pathToVideoFolder+lines+sourceVideoFormat+'\'' +'\n')

def WriteToTextfile2(path,text):
    videoPath = path

    file = open(pathToVideoList, 'w')

    for lines in text:
        file.write('file \''+videoPath+lines+sourceVideoFormat +'\n')

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('pk', 'created','name','content','rating')


    def create(self, validated_data):
        return Features.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name) 
        instance.content = validated_data.get('content', instance.content)    
        instance.rating = validated_data.get('rating', instance.rating)    

        instance.save()
        return instance