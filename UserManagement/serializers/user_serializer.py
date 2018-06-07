from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer

from ..models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'pwd', 'stat', 'name_used_before', 'sex', 'birthday',
                  'political', 'native_place', 'phone_number', 'country_and_region', 'creator']