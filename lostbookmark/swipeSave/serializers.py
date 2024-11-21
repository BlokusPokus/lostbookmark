# Serializer are for converting querysets to python objects
from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['url', 'title', 'description']
