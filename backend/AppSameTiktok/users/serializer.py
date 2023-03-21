from .models import Users
from rest_framework import serializers
from rest_framework.authtoken.views import Token
import requests
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields ='__all__'
        extra_kwargs = {'password':{
            'write_only':True,
        }}
        
        
         
    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
    
      
        
        
        
    
        