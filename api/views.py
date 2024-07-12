from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article
from django.contrib.auth import get_user_model
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import status
from .permissions import IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['status', 'author__username']
    search_fields = ['title', 'content', 'author__username',]
    ordering_fields = ['status', 'published_at']



    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrStaffReadOnly]







class CustomConfirmEmailView(TemplateView):
    template_name = 'account_confirm_email.html'



