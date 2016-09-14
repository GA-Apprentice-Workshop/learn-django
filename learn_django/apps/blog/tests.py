from django.test import TestCase
from django.urls import reverse
from .factories import AuthorFactory, BlogFactory

# Create your tests here.


class TestBlogView(TestCase):
    def setup(self):
        self.author = AuthorFactory()
        self.blog = BlogFactory(author=self.author)

    def test_index_success(self):
        res = self.client.get('/')

        self.assertEqual(res.status_code, 200)

    def test_create_blog(self):
        author = AuthorFactory()
        data = {
            'title': "A New Blog",
            'text': "This is a new blog with text.",
            'author': author
        }
        # url = reverse('blog_view', data)
        res = self.client.post('blog/new/', data)

        self.assertEqual(res.status_code, 201)
