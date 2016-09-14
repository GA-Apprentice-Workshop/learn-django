from django.http import HttpResponse
from django.views.generic import ListView

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Author, Blog
from .serializers import AuthorSerializer, BlogSerializer


class BlogView(ListCreateAPIView):
    """
    GET: Returns a list of all blogs. Returns HTTP 200/400
    POST: Creates new blog entries. Returns HTTP 201/400

    For custom responses, use .list method.

    APIView docs: http://www.django-rest-framework.org/api-guide/generic-views/
    """
    model = Blog
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

blog_view = BlogView.as_view()


class AuthorView(RetrieveUpdateAPIView):
    """
    GET: Returns instance of author. Returns HTTP 200/400
    PUT/PATCH: Edits author instance. Returns HTTP 200/400

    For custom PUT responses, use .update method. For custom PATCH responeses,
    use .partial_update.
    """
    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

author_view = AuthorView.as_view()
