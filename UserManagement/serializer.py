from rest_framework import serializers
from UserManagement.models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'pwd')
<<<<<<< HEAD


class UserLoginLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserLoginLog
        fields = ('id', 'time', 'user')


class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('name', 'description')
=======
>>>>>>> 9ec56b0552ed3ae9bb5351c316795c332c080acb
