from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer

from ..models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'pwd', 'stat', 'creator']