from django.shortcuts import render
from blog.models import Article
from .serializers import ArticleSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.


class ArticleListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

