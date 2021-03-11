from rest_framework import serializers
from news.models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'link', 'author_name', 'creation_date', ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ['author_name', 'creation_date', 'content', 'post_id']
