"""
learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from learn_django.portal import views

urlpatterns = [
    # Django expects to send requests to a callable function.
    # Therefore class-based views have an as_view() function
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.index_view, name='home'),
    # url('^', include('django.contrib.auth.urls')),
    # url(r'^login/$', views.login_view, name='home'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^blog/', include('learn_django.blog.urls')),
    # JWT Auth
    url(r'^auth/', obtain_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
    # API
    url(r'^api/v1/', include('learn_django.api_urls')),
]
