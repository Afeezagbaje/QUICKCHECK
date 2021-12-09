from rest_framework import serializers
from .models import Story, Comment


class StorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Story
        fields = ["id", "author", "descendants", "score", "type", "title", "url"]


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "author", "text"]
