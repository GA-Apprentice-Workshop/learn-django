
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework.generics import CreateAPIView

from .forms import LoginForm

class IndexView(TemplateView):
    template_name = 'index.html'

index_view = IndexView.as_view()


class LoginView(View):
    """
    Custom:
    https://docs.djangoproject.com/en/1.10/topics/auth/default/#authenticating-users

    Built-in:
    https://github.com/django/django/blob/master/django/contrib/auth/views.py
    https://docs.djangoproject.com/en/1.10/topics/auth/default/#module-django.contrib.auth.views
    """

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        msg = messages.add_message(request, messages.INFO, 'Try again.')
        username, auth = (request.POST['username'], request.POST['auth'])
        user = authenticate(username=username, password=auth)

        print(user)

        if user is not None:
            login(request, user)
            print("{} has been logged in.".format(user))
            return HttpResponseRedirect('/blog/')
        else:
            return render(request, 'login.html', {'form': LoginForm(), 'messages': msg})

login_view = LoginView.as_view()


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class SignupView(CreateView):
    """
    Creates an instance of User.
    """
    model = User
    fields = ['username', 'email', 'password']
    success_url = 'profile/'
    template_name_suffix = '_create_form' # TODO: Create template

signup_view = SignupView.as_view()


class ProfileView(UpdateView):
    """
    View user profile to chane things like password.
    """
    model = User
    fields = ['username','email', 'password']
    template_name_suffix = '_update_form' # TODO: Create template

profile_view = ProfileView.as_view()
