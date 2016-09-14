from django.conf.urls import url
from learn_django.apps.blog.views import blog_view

urlpatterns = [
    url(r'^$', blog_view, name='blog_view'),
]
