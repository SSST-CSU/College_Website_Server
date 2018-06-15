from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet

from ..models.Teacher import *
from ..serializers.teacher_serializer import *

import json


class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()