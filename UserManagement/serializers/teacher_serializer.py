from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer

from ..models.Teacher import *
from .user_serializer import UserSerializer


class TeacherSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Teacher
        fields = ['id', 'name', 'pwd', 'stat', 'name_used_before', 'sex', 'birthday',
                  'political', 'native_place', 'id_number', 'phone_number', 'country_and_region',
                  'title', 'is_external_unit']
