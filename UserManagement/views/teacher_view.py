from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet

from ..models.Teacher import *
from ..serializers.teacher_serializer import *
from .user_view import UserViewSet

import json


class TeacherViewSet(UserViewSet):
    serializer_class = TeacherSerializer

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        queryset = Teacher.objects.none()
        perm = False

        if 'UserManagement.view_my_teachers' in perm_set or 'UserManagement.view_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Teacher.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.view_department_teachers' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Teacher.objects.get_department_user(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.view_all_teachers' in perm_set or 'UserManagement.view_all_users' in perm_set:
            queryset = Teacher.objects.all()
            perm = True

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(TeacherViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_teacher' in perm_set or 'UserManagement.create_user' in perm_set:
            return super(TeacherViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        queryset = Teacher.objects.none()
        perm = False

        if 'UserManagement.update_my_teachers' in perm_set or 'UserManagement.update_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Teacher.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.update_department_teachers' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Teacher.objects.get_department_user(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.update_all_teachers' in perm_set or 'UserManagement.update_all_users' in perm_set:
            queryset = Teacher.objects.all()
            perm = True

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(TeacherViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        queryset = Teacher.objects.none()
        perm = False

        if 'UserManagement.delete_my_teachers' in perm_set or 'UserManagement.delete_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Teacher.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.delete_department_teachers' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Teacher.objects.get_department_user(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.delete_all_teachers' in perm_set or 'UserManagement.delete_all_users' in perm_set:
            queryset = Teacher.objects.all()
            perm = True

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(TeacherViewSet, self).destroy(request, *args, **kwargs)