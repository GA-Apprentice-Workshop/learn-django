import factory

from .models import Author, Blog


class BlogFactory(factory.Factory):
    class Meta:
        model = Blog

    title = "Test Blog Title"
    text = "This is a single blog entry. It has two sentences."


class AuthorFactory(factory.Factory):
    class Meta:
        model = Author

    name = "Blogger McBloggin" \
