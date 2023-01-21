from unicodedata import name
from venv import create
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    group = models.IntegerField()
    create = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now_add = True)
    is_published = models.BooleanField(default = True)
    cat = models.ForeignKey('Category', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    
    
