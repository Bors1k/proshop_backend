from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.username
        token['email'] = user.email

        return token