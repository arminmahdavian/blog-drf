from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article, User
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import generics, status
from .permissions import IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
from django.views.generic import TemplateView


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


class CustomConfirmEmailView(TemplateView):
    template_name = 'account_confirm_email.html'
    # def get(self, request, *args, **kwargs):
    #     print("--------------------------------")
    #     print("CustomConfirmEmailView called")
    #     print("--------------------------------")
    #     return super().get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        key = kwargs.get('key')  # Access the captured key from the URL
        print("--------------------------------")
        print(f"CustomConfirmEmailView called with key: {key}")
        print("--------------------------------")
        return super().get(request, *args, **kwargs)

    def get_template_names(self):
        return [self.template_name]


