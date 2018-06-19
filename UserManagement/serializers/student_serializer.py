from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer

from .user_serializer import UserSerializer

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


class UndergraduateStudentSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Undergraduate_Student
        fields = super().fields + ['student_class']


class GraduateStudentSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Graduate_Student
        fields = super().fields + ['student_class', 'instructor', 'on_the_job', 'company']