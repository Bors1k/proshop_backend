from dataclasses import field
from pyexpat import model
from queue import Empty
from rest_framework import serializers
from base import models
from .models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        serializers = UserSerializerWithToken(user).data
        for k,v in serializers.items():
            token[k] = v

        return token

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.UserProfile
        fields = ['id','email','name', 'is_staff']

    def get_name(self,obj):
        name = obj.name
        if name == '':
            name = obj.email

        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta: 
        model = models.UserProfile
        fields = ['id','email','name', 'is_staff', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)