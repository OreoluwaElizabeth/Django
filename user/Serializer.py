from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import TokenCreateSerializer, TokenSerializer as BaseUserLoginSerializer
from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']


class UserLoginSerializer(BaseUserLoginSerializer):
    fields = ['email', 'password']
