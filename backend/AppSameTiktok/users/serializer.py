from .models import Users, UserProfile
from rest_framework import serializers
from rest_framework.authtoken.views import Token
import requests


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields ='__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=True)
    class Meta:
        
        model = Users
        fields =['username', 'first_name', 'last_name', "phone_number", 'email','role_user','profile']
        extra_kwargs = {'password':{
            'write_only':True,
        }}
        
        
         
    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        user_profile =  UserProfile.objects.create(user_id=user.id)
        return user
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
    

        
        
      
        
        
        
    
        