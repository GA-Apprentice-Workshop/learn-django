from django.test import TestCase
from django.urls import reverse
from .factories import UserFactory


class TestPortalView(TestCase):
    """
    Test generic user functionality such as signing in, signing up,
    and permission.
    """
    def setup(self):
        self.user = UserFactory()

    def test_login_view(self):
        user = UserFactory(username='newbie')
        user.set_password('newpassword')
        response = self.client.login(username=user.username, password=user.password)

        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        pass

    def test_profile_view(self):
        pass
