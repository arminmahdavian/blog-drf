from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, basename="users")
router.register(r'articles', views.ArticleViewSet, basename="articles")

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),

]

