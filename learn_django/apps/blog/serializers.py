from rest_framework import serializers

from .models import Author, Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['author', 'title', 'text', 'modified']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['uuid', 'username']
