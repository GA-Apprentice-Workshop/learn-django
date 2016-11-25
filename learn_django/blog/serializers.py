from rest_framework import serializers

from .models import Author, Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('author', 'title', 'text', 'modified')


class AuthorSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True)

    class Meta:
        model = Author
        fields = ('first_name', 'blogs')
