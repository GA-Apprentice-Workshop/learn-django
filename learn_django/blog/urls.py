from django.conf.urls import url

from learn_django.blog import views

urlpatterns = [
    url(r'^$', views.blog_view, name='blog_view'),
    url(r'^author/(?P<pk>[0-9]+)/$', views.author_view, name='author_view'),
]
