from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article, User
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import generics, status
from .permissions import IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly


# Create your views here.


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly, IsStaffOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class UserListView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUserOrStaffReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsSuperUserOrStaffReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

