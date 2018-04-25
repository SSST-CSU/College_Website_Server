from rest_framework import serializers
from UserManagement.models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'pwd')
