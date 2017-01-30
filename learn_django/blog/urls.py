from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from learn_django.blog import views

urlpatterns = [
    url(r'^$', views.blog_view, name='blog_view'),
    url(r'^author/(?P<pk>[0-9]+)/$', views.author_view, name='author_view'),
]

router = DefaultRouter()
router.register('blogs', views.BlogViewSet)
router.register('author', views.AuthorViewSet)

urlpatterns += router.urls
