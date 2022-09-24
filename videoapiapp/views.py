from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import video, comments
from .serializer import VideoSerializer, CommentSerializer
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
class allvideos(APIView):
    parse_classes = (MultiPartParser, FormParser)
    def get(self, request):
        postedvideos = video.objects.all()
        serializer = VideoSerializer(postedvideos, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        
        serializers = VideoSerializer(data=request.data)
 
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,
            status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, 
            status=status.HTTP_400_BAD_REQUEST)

class commentvideos(APIView):
    def get(self, request, pk):
        commentedvideos = comments.objects.filter(visitorspost_id=pk)
        serializer = CommentSerializer(commentedvideos, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        
        comment_serializers = CommentSerializer(data=request.data)
 
        if comment_serializers.is_valid():
            comment_serializers.save()
            return Response(comment_serializers.data,
            status=status.HTTP_201_CREATED)
        else:
            return Response(comment_serializers.errors, 
            status=status.HTTP_400_BAD_REQUEST)

