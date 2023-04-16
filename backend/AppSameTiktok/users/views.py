
from .models import Users, UserProfile
from rest_framework import status, viewsets
from .serializer import UserSerializer, ProfileSerializer, TokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import Token
from rest_framework.decorators import api_view

from datetime import datetime
from rest_framework import status
from django.conf import settings
import requests


class UserViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    
class ProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    
    
def get_user(request, username, password):
    username = username
    password = password
    
    auth_login = settings.LINK_API + "/users/auth/"
    query_string = {
        "username": username,
        "password": password,   
    }
    user = None
    token = None
    try:
        auth_response =  requests.request("POST", auth_login,  json=query_string)
        token = auth_response.json()['token']
    except:
        return user, token
    
    token_user = Token.objects.get(key = token)
    user = Users.objects.get(id = token_user.user_id)
    token_user.delete()
    token = Token.objects.create(user=user)
    return user,token
    
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
def login_user(request):
    username = request.data['username']
    password = request.data['password']
    user,token = get_user(request=request,username=username, password=password)
    message = {}
    if user == None:
        message['error'] = "Tài khoản hoặc mật khẩu không chính xát"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    date = datetime.now()
    user.last_login = date
    user.save()
    serializer = UserSerializer(user)
    message['data'] = serializer.data
    token_serializer =  TokenSerializer(token)
    message['token'] = token_serializer.data
    return Response(message, status=status.HTTP_202_ACCEPTED)
    
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
        token = Token.objects.create(user=user)
        user_profile =  UserProfile.objects.create(user=user)
        user = Users.objects.get(id= user.id)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
    except:
        message = {}
        message['error'] = "Có lỗi xảy ra vui lòng thử lại sau"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
         

@api_view(['PUT'])
def update_name(request):
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    token = request.data['token']
    
    message = {}
    user = get_user_update(request=request,token=token)
    if user == None:
        message['error'] = "Có lỗi xảy ra vui lòng thử lại"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    message['success'] = "Cập nhập tên thành công"
    return Response(message, status=status.HTTP_202_ACCEPTED)

@api_view(['PUT'])
def update_phone(request):
    phone_number = request.data['phone_number']
    token = request.data['token']
    
    message = {}
    user = get_user_update(request=request,token=token)
    if user == None:
        message['error'] = "Có lỗi xảy ra vui lòng thử lại"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    user.phone_number = phone_number
    user.save()
    message['success'] = "Cập nhập số điện thoại thành công"
    return Response(message, status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
def update_email(request):
    email = request.data['email']
    token = request.data['token']
    
    message = {}
    user = get_user_update(request=request,token=token)
    if user == None:
        message = {}
        message['error'] = "Có lỗi xảy ra vui lòng thử lại"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
        
    user.email = email
    user.save()
    message['success'] = "Cập email thành công"
    return Response(message, status=status.HTTP_202_ACCEPTED)
    
@api_view(['PUT'])
def update_profile_picture(request):
    profile_picture = request.data['profile_picture']
    token = request.data['token']
    message = {}
    user = get_user_update(request=request,token=token)
    if user == None:
        message = {}
        message['error'] = "Có lỗi xảy ra vui lòng thử lại"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    user_profile = UserProfile.objects.get(user_id = user.id)    
    user_profile.profile_picture = profile_picture
    user_profile.save()
    message['success'] = "Cập nhập profile thành công"
    return Response(message, status=status.HTTP_202_ACCEPTED)

@api_view(['PUT'])
def update_profile_sex(request):
    profile_sex = request.data['profile_sex']
    token = request.data['token']
    message = {}
    user = get_user_update(request=request,token=token)
    if user == None:
        message = {}
        message['error'] = "Có lỗi xảy ra vui lòng thử lại"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    user_profile = UserProfile.objects.get(user_id = user.id)    
    user_profile.sex = profile_sex
    user_profile.save()
    message['success'] = "Cập nhập profile thành công"
    return Response(message, status=status.HTTP_202_ACCEPTED)
    
@api_view(['PUT'])
def update_full_address(request):
    profile_country = request.data['profile_country']
    profile_city = request.data['profile_city']
    profile_district = request.data['profile_district']
    profile_state = request.data['profile_state']
    profile_address = request.data['profile_address']
    token = request.data['token']
    message = {}
    user = get_user_update(request=request,token=token)
    if user == None:
        message = {}
        message['error'] = "Có lỗi xảy ra vui lòng thử lại"
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    user_profile = UserProfile.objects.get(user_id = user.id)    
    user_profile.country = profile_country
    user_profile.city = profile_city
    user_profile.district = profile_district
    user_profile.state = profile_state
    user_profile.address = profile_address
    user_profile.save()
    message['success'] = "Cập nhập profile thành công"
    return Response(message, status=status.HTTP_202_ACCEPTED)
    
    
    
    
    
         
    
    