from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer

from ..models.Student import *


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['name']


class StudentGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Grade
        fields = ['name', 'major']


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Class
        fields = ['name', 'grade', 'headmaster', 'instructor']