import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User


class Blog(models.Model):
    """
    Creates an instace of :model:`blog.Blog`, which is an article submitted by Authors.
    """
    author = models.ForeignKey('Author', related_name='blogs')
    title = models.CharField(max_length=75)
    text = models.TextField(help_text='Content of the blog entry. May include HTML.')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)


class CustomUserManager(BaseUserManager):
    """
    Custom management for the :model:`blog.Author` model.
    """
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
    """
    Creates an instance of :model:`blog.Author` based on :model:`auth.User`. Provides
    is_staff permissions for blog editors.
    """
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
