import factory
from django.contrib.auth.models import User

class UserFactory(factory.Factory):
    username = 'mcuser'
    password = 'slimshady'

    class Meta:
        model = User
