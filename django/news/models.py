from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, blank=True)
    amount_of_upvotes = models.PositiveSmallIntegerField(default=0)
    author_name = models.CharField(max_length=150, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveSmallIntegerField(default=0)
    link = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['creation_date']


class Comment(models.Model):
    author_name = models.CharField(max_length=150, blank=True, default='')
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post_id = models.ForeignKey('Post', related_name='post_id', on_delete=models.CASCADE)

    class Meta:
        ordering = ['creation_date']
