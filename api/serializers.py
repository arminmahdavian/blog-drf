from rest_framework import serializers

from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        # fields = ('title', 'slug', 'author', 'content', 'published_at')
        # exclude = ('created_at', 'updated_at')
        fields = '__all__'


