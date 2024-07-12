from rest_framework import serializers
from django.contrib.auth import get_user_model
from blog.models import Article
from drf_dynamic_fields import DynamicFieldsMixin




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class AuthorUsernameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    def get_author(self, obj):
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name
        }

    author = serializers.SerializerMethodField("get_author")
    class Meta:
        model = Article
        # fields = ('title', 'slug', 'author', 'content', 'published_at')
        # exclude = ('created_at', 'updated_at')
        fields = '__all__'

    def validate_title(self, value):
        filter_list = ["javascript",]

        for item in filter_list:
            if item.lower() in value.lower():
                raise serializers.ValidationError('Title contains inappropriate word. : {}'.format(item))






