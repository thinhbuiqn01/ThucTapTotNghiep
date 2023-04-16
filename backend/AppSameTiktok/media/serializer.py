from .models import Media
from rest_framework import serializers
from rest_framework.authtoken.views import Token
import requests
class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields ='__all__'