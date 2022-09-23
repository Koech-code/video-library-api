from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField
from .models import video, comments

class VideoSerializer(serializers.ModelSerializer):
    video = FileField()
    class Meta:
        model = video
        fields = ('name', 'video', 'description')