import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User


class Blog(models.Model):
    author = models.ForeignKey('Author', related_name='blogs')
    title = models.CharField(max_length=75)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, **kwargs):
        user = self.model(
            is_staff=True,
            **kwargs
        )
        if not kwargs.get('password'):
            password = self.make_random_password()
            user.set_password(password)

        user.save()
        return user


class Author(User):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)

    USERNAME_FIELD = 'uuid'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = CustomUserManager()

    class Meta:
        """
        Settings:
        abstract = True means no table will be created in database!
        app_label = If this will be part of a different app such as the portal
        """
        ordering = ('last_name',)

    def _repr_(self):
        return "{0.first_name} {0.last_name} <{0.email}>".format(self)
