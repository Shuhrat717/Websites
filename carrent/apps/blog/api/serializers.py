from rest_framework import serializers
from ..models import Blog


class ArticleGetSerialize(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'category', 'title', 'content', 'tags',  'created_at']


class ArticleSerialize(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'category', 'title', 'image', 'content', 'tags',  'created_at']
