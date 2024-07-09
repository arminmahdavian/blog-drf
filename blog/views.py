from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, User


# Create your views here.


class ArticleListView(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(
            Article.objects.all(),
            pk=self.kwargs.get('pk')
            # slug=self.kwargs.get('slug')
        )


class UserListView(ListView):
    def get_queryset(self):
        return User.objects.all()


class UserDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(
            User.objects.all(),
            pk=self.kwargs.get('pk')
        )





