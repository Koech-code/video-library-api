from rest_framework import serializers
from .models import video, comments

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ('name', 'video', 'description')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = ('visitorspost', 'visitorscomment')