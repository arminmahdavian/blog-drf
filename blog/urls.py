from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    # path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]

