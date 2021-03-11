from celery import shared_task
from news.models import Post, Comment
from test.celery import app
from celery.schedules import crontab



@shared_task
def add(x, y):
    return x + y


@app.task
def change_content():
    comments = Comment.objects.all()
    for each in comments:
        each.content += "arg"
        each.save()
    return "success"
