from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'news', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path("example_celery_delay",  views.example_celery_delay, name='example_celery_delay'),
    path("example_celery_model",  views.example_celery_model, name='example_celery_model')
]
