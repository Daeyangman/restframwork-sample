from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer
from rest_framework import generics

# class PostViewSet(viewsets.ModelViewSet):
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
