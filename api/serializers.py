from rest_framework import serializers
from django.contrib.auth import get_user_model
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        # fields = ('title', 'slug', 'author', 'content', 'published_at')
        # exclude = ('created_at', 'updated_at')
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'




