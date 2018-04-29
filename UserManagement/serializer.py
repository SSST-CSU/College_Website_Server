from rest_framework import serializers
from UserManagement.models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'pwd')


class UserLoginLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserLoginLog
        fields = ('id', 'time', 'user')


class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('name', 'description')
