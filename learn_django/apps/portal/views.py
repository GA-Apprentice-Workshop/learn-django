
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from rest_framework.generics import CreateAPIView

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
