"""
ViewSet is used with rest_framework.routers
    http://www.django-rest-framework.org/api-guide/viewsets/#viewset

    For custom routing use:
    from rest_framework.decorators import detail_route, list_route

    @list_route() ; @detail_route()
    @list_route(methods=[], permission_classes=[], url_path='')

    ModelViewSet methods:
        * list
        * create
        * retrieve
        * update
        * partial_update
        * destroy
    http://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

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
    # lookup_field = 'uuid'

author_view = AuthorView.as_view()


class BlogViewSet(ModelViewSet):
    """
    API viewset for Blog.
    """
    model = Blog
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (TemplateHTMLRenderer,)

    def retrieve(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'blog': self.object}, template_name='blog/show.html')


class AuthorViewSet(ModelViewSet):
    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
