from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name']


class RoomBorrowingApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBorrowingApply
        fields = ['user', 'room', 'start_time', 'end_time']