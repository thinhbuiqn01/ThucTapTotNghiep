from .models import Post
from media.models import Media 
from users.models import Users
from rest_framework.authtoken.views import Token
from rest_framework import status, viewsets
from .serializer import PostSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from datetime import datetime
from rest_framework import status
from django.conf import settings
import requests

class Postviewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    
def get_user_update(request, token):
    user = None
    user_token = None
    try:
        user_token = Token.objects.get(key=token)
        print("aaa")
        user = Users.objects.get(id = user_token.user_id)
    except:
        return user
    return user
    
@api_view(['GET'])
def post_list(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    print(serializer.data)
    return Response(serializer.data)
@api_view(['POST'])
def post_add(request):
    title = request.data['title']
    media = request.data['media']
    token = request.data['token']
    user = get_user_update(request=requests, token=token)
    message = {}
    try:
        post = Post.objects.create(title = title, user_id = user.id)
        media = Media.objects.create(title = title, post_id = post.id, media= media)
    except:
        message['error'] = "Có lỗi khi thêm bài đăng!"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    post_serializer = PostSerializer(post)
    return Response(post_serializer.data,status=status.HTTP_202_ACCEPTED)
    
    
@api_view(['PUT'])
def post_update(request):
    post_id = request.data['post_id']
    title = request.data['title']
    media = request.data['media']
    token = request.data['token']
    user = get_user_update(request=request, token=token)
    if user == None:
         message['error'] = "Có lỗi khi cập nhập bài viết aaa!"
         return Response(message, status=status.HTTP_400_BAD_REQUEST)
    message = {}
    try:
        post = Post.objects.get(id = post_id)
        post.title = title
        medias = Media.objects.get(post_id = post.id)
        medias.title =title
        medias.media = media
        post.save()
        medias.save()
    except:
        message['error'] = "Có lỗi khi cập nhập bài viết!"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    post_serializer = PostSerializer(post)
    return Response(post_serializer.data,status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
def post_update_title(request):
    post_id = request.data['post_id']
    title = request.data['title']
    token = request.data['token']
    user = get_user_update(request=request, token=token)
    message = {}
    if user == None:
         message['error'] = "Có lỗi khi cập nhập bài viết!"
         return Response(message, status=status.HTTP_400_BAD_REQUEST)
    try:
        post = Post.objects.get(id = post_id)
        post.title = title
        medias = Media.objects.get(post_id = post.id)
        medias.title =title
        post.save()
        medias.save()
    except:
        message['error'] = "Có lỗi khi cập nhập bài viết!"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    post_serializer = PostSerializer(post)
    return Response(post_serializer.data,status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def post_delete(request):
    post_id = request.data['post_id']
    token = request.data['token']
    user = get_user_update(request=request, token=token)
    if user == None:
         message['error'] = "Có lỗi khi cập nhập bài viết!"
         return Response(message, status=status.HTTP_400_BAD_REQUEST)
    message = {}
    try:
        post = Post.objects.get(id = post_id)
        medias = Media.objects.get(post_id = post_id)
        post.delete()
        medias.delete()
    except:
        message['error'] = "Có lỗi khi cập nhập bài viết!"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    message['success'] = "Xóa bài viết thành công"
    return Response(message,status=status.HTTP_202_ACCEPTED)

