from ..models.Department import *
from ..models.User_Duty import *
from ..models.Duty_Department import *


from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer


class DutyDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duty_Department
        fields = ['duty', 'department']


class UserDutySerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Duty
        fields = ['user', 'duty']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Duty
        fields = ['name', 'superior']