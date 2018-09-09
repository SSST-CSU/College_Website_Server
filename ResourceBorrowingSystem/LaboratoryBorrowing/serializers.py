from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer
from .models import *


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = ['name']


class LaboratoryApplyReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryApplyReason
        fields = ['reason']


class LaboratoryBorrowingApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryBorrowingApply
        fields = ['apply_id', 'user', 'room', 'apply_time', 'update_time', 'reason_type', 'reason', 'start_time', 'end_time', 'stat']
