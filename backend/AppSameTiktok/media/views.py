from .models import Media
from rest_framework import status, viewsets
from .serializer import MediaSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from datetime import datetime
from rest_framework import status
from django.conf import settings
import requests

class Mediaviewset(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer