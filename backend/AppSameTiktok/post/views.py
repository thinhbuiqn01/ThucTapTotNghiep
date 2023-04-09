from .models import Post
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
    
    
@api_view(['GET'])
def allpost(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    print(serializer.data)
    return Response(serializer.data)
    


