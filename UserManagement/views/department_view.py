from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet

from ..models.Duty_Department import *
from ..models.User_Duty import *
from ..models.Department import *
from ..serializers.department_serializer import *

import json


class DutyDepartmentViewSet(ModelViewSet):
    serializer_class = Duty_Department
    queryset = Duty_Department.objects.all()

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.view_duty_departments' in perm_set:
            return super(DutyDepartmentViewSet, self).list(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_duty_department' in perm_set:
            return super(DutyDepartmentViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.update_duty_departments' in perm_set:
            return super(DutyDepartmentViewSet, self).update(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.delete_duty_departments' in perm_set:
            return super(DutyDepartmentViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class UserDutyViewSet(ModelViewSet):
    serializer_class = User_Duty
    queryset = User_Duty.objects.all()

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.view_user_duties' in perm_set:
            return super(UserDutyViewSet, self).list(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_user_duty' in perm_set:
            return super(UserDutyViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.update_user_duties' in perm_set:
            return super(UserDutyViewSet, self).update(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.delete_user_duties' in perm_set:
            return super(UserDutyViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class DepartmentViewSet(ModelViewSet):
    serializer_class = Department
    queryset = Department.objects.all()

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.view_dept' in perm_set:
            return super(DepartmentViewSet, self).list(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_dept' in perm_set:
            return super(DepartmentViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.update_dept' in perm_set:
            return super(DepartmentViewSet, self).update(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.delete_dept' in perm_set:
            return super(DepartmentViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
