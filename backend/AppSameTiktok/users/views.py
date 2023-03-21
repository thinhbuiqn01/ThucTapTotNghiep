
from .models import Users
from rest_framework import status, viewsets
from .serializer import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import Token
from rest_framework.decorators import api_view
from django.http import HttpResponse

from datetime import datetime
from rest_framework import status
from django.conf import settings
import requests


class UserViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    
@api_view(['GET'])
def login_user(request):
    username = request.data['username']
    password = request.data['password']
    auth_login = settings.LINK_API + "/users/auth/"
    query_string = {
        "username": username,
        "password": password,   
    }
    message = {}
    try:
        auth_response =  requests.request("POST", auth_login,  json=query_string)
        token = auth_response.json()['token']
    except:
        message['error'] = "Tên tài khoản của bạn hoặc Mật khẩu không đúng, vui lòng thử lại"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    token_user = Token.objects.get(key = token)
    user = Users.objects.get(id = token_user.user_id)
    date = datetime.now()
    user.last_login = date
    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
@api_view(['POST'])
def register_user(request):
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']
    
    users = Users.objects.all()
    for u in users:
        if email == u.email:
            message = {}
            message['error'] = "Email đã được đăng kí"
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
        if username == u.username:
            message = {}
            message['error'] = "Username đã tồn tại"
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    try:
        user  = Users.objects.create_user(username=username, email=email, password=password)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
    except:
        message = {}
        message['error'] = "Có lỗi xảy ra vui lòng thử lại!"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
         
    
    
    