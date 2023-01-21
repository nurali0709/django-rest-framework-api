from ast import Delete
from csv import field_size_limit
from dataclasses import fields
from email.policy import default
from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Article
        fields = ('__all__')