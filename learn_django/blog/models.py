import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User


class Blog(models.Model):
    """
    Creates an instace of :model:`blog.Blog`, which is an article submitted by Authors.

    About Related Objects:
    https://docs.djangoproject.com/en/1.10/ref/models/relations/

    Author.blog methods: .add(), .create(), clear(), .remove(), .all(), .set()
    """
    author = models.ForeignKey('Author', related_name='blogs')
    title = models.CharField(max_length=75)
    text = models.TextField(help_text='Content of the blog entry. May include HTML.')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "{0.title}".format(self)


class CustomUserManager(BaseUserManager):
    """
    Custom management for the :model:`blog.Author` model.

    Learn more about :model: `django.contrib.auth.models.User` model
    https://docs.djangoproject.com/en/1.10/topics/auth/default/#user-objects

    """
    def create_user(self, username, **kwargs):
        user = self.model(
            username=username,
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
    # Make a charfield so Django won't complain about TypeErrors from UI
    uuid = models.CharField(primary_key=True, default=uuid.uuid4, unique=True, max_length=32)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = CustomUserManager()

    class Meta:
        """
        Settings:
        abstract = True means no table will be created in database!
        app_label = If this will be part of a different app such as the portal
        """
        ordering = ('last_name',)

    def _str_(self):
        return "{0.first_name} {0.last_name} <{0.email}>".format(self)
