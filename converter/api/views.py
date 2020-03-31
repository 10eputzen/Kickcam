from rest_framework import generics
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from django.http import HttpResponse
from subprocess import Popen
import subprocess


def Start(request, *args, **kwargs):
    print ("Stop Recording if already running")
    process = subprocess.Popen('pkill raspivid', stdout=subprocess.PIPE, shell=True)
    process = subprocess.Popen('raspivid -o ../html/video/currentReplay/currentReplay.h264 -t 600000 -w 1280 -h 720', stdout=subprocess.PIPE, shell=True)
    #pkill raspivid
    return HttpResponse()

def Stop(request, *args, **kwargs):
    print ("Stop Recording")
    process = subprocess.Popen('pkill raspivid', stdout=subprocess.PIPE, shell=True)
    return HttpResponse()