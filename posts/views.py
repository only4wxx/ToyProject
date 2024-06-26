from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer, AllPostSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class PostList(APIView):
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        posts = Post.objects.all().order_by('-created_at') # 시간 내림차순 정렬
        serializer = AllPostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetail(APIView):
     def get(self, request, id): # 게시글 하나 불러오기
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
     
     def delete(self, request, id): # 게시글 하나 삭제하기
        post = get_object_or_404(Post, id=id)
        if post.password == request.data['password']: # 올바른 비밀번호를 입력하면 삭제 가능
            post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)