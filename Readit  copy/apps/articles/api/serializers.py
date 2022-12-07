from rest_framework import serializers
from ..models import Article


class ArticleGetSerialize(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'category', 'title', 'get_image_url', 'context', 'tags',  'created_at']


class ArticleSerialize(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'category', 'title', 'image', 'context', 'tags',  'created_at']
