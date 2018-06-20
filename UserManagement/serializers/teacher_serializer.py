from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer

from ..models.Teacher import *
from .user_serializer import UserSerializer


class TeacherSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Teacher
        fields = super().fields + ['title', 'is_external_unit']
