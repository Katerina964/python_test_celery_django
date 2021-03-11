
from rest_framework import viewsets
from rest_framework.decorators import action
from news.models import Post, Comment
from news.serializers import PostSerializer, CommentSerializer
from .tasks import add, change_content
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@csrf_exempt
def example_celery_delay(request):
    if request.method == "GET":
        x = 1
        y = 2
        result = add.delay(x,y)
        return  HttpResponse(f"equal {result.get()}")
    return HttpResponse("Nothing")


@csrf_exempt
def example_celery_model(request):
    if request.method == "GET":
        result = change_content.delay()
        return  HttpResponse(f"equal {result.get()}")
    return HttpResponse("Nothing")

    
