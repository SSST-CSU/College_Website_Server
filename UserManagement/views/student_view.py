from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet

from ..models.Student import *
from ..serializers.student_serializer import *
from .user_view import UserViewSet

import json


class MajorViewSet(ModelViewSet):
    serializers_class = Major
    queryset = Major.objects.all()

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.view_major' in perm_set:
            return super(MajorViewSet, self).list(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_major' in perm_set:
            return super(MajorViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.update_major' in perm_set:
            return super(MajorViewSet, self).update(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.delete_major' in perm_set:
            return super(MajorViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class UndergraduateStudentViewSet(UserViewSet):
    pass
