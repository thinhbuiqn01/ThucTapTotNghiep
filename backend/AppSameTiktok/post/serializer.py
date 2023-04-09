from .models import Post
from rest_framework import serializers
from rest_framework.authtoken.views import Token
import requests
from media.serializer import MediaSerializer


class PostSerializer(serializers.ModelSerializer):
    # media = MediaSerializer(many=True,
    #     read_only=True
    # )
    
    medias=MediaSerializer(many=True)
    class Meta:
        model = Post
        # fields ='__all__'
        fields =('id','title','user', 'medias')

    