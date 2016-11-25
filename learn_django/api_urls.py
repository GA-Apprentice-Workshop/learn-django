"""
Django REST Framework Routingg

DefaultRouter auto generates restful endpoints using the
name derived from the queryset property of the view.

ViewSet is required for usage.
"""
from rest_framework.routers import DefaultRouter

from learn_django.blog.views import BlogViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register('authors', AuthorViewSet)

urlpatterns = router.urls
