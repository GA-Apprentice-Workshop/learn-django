
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView

from .forms import LoginForm


class LoginView(View):
    """
    https://docs.djangoproject.com/en/1.10/topics/auth/default/#authenticating-users
    """

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        username, auth = (request.user, request.POST['auth'])
        user = authenticate(username=username, password=auth)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/blog/')
        else:
            return HttpResponseRedirect('/')

login_view = LoginView.as_view()