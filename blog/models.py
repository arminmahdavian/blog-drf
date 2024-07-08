from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title



