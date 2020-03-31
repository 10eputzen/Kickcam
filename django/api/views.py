from api.models import Replay
from api.serializers import ReplaySerializer
from api.models import Features
from api.serializers import FeaturesSerializer

from rest_framework import generics
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from django.http import HttpResponse
from subprocess import Popen
import subprocess


class ReplayList(generics.ListCreateAPIView):
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer
    #def perform_create(self, serializer):
     #   serializer.save(owner=self.request.user)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReplayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
     #                 IsOwnerOrReadOnly,)

class FeaturesList(generics.ListCreateAPIView):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer

class FeaturesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer

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