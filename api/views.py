from tokenize import Token
from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ArticleListAPI(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ArticleUpdateAPI(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )
    #authentication_classes = (TokenAuthentication, )

class ArticleDeleteAPI(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )