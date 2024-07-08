from django.urls import path, include
from .views import ArticleListView


app_name = 'api'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),

]

