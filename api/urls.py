from django.urls import path, include
from . import views


app_name = 'api'

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='list'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    # path('articles/<slug:slug>', ArticleDetailView.as_view(), name='list'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

]

