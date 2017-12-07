from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
class PostListAPIView(APIView):
    def get(self ,request):
        serializer = PostSerializer(Post.objects.all() , many= True)
        return Response(serializer.data)
    def post(self , request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status = 201)
        return Response(serializer.errors, status= 400)

class LoginendTemplateView(TemplateView):
    template_name = 'registration/login_end.html'

class MypageTemplateView(TemplateView):
    template_name = 'mypage.html'

class EEGListView(ListView):
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.all().values()
