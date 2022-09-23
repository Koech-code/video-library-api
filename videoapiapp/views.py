from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
from .models import video, comments
from .serializer import VideoSerializer

# Create your views here.
class allvideos(APIView):
    parser_classes = [FileUploadParser]
    def get(self, request):
        postedvideos = video.objects.all()
        serializer = VideoSerializer(postedvideos, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        video_file = request.FILES['file']
        destination = open('/Users/Username/' + video_file.name, 'wb+')
        for chunk in video_file.chunks():
            destination.write(chunk)
        destination.close()  
        return Response(video_file.name, status.HTTP_201_CREATED)
