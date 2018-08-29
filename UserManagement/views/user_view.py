from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet

from ..models.User import User
from ..serializers.user_serializer import UserSerializer

import json


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        queryset = User.objects.none()
        perm = False

        if 'UserManagement.view_all_users' in perm_set:
            perm = True
            queryset = queryset | User.objects.all()

        if 'UserManagement.view_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | User.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.view_class_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | User.objects.get_class_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.view_grade_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | User.objects.get_grade_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(UserViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_user' in perm_set:
            return super(UserViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        queryset = User.objects.none()
        perm = False

        if 'UserManagement.update_all_users' in perm_set:
            perm = True
            queryset = queryset | User.objects.all()

        if 'UserManagement.update_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | User.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.update_class_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | User.objects.get_class_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.update_grade_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | User.objects.get_grade_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(UserViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        queryset = User.objects.none()
        perm = False

        if 'UserManagement.delete_all_users' in perm_set:
            perm = True
            queryset = queryset | User.objects.all()

        if 'UserManagement.delete_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | User.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.delete_class_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | User.objects.get_class_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.delete_grade_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | User.objects.get_grade_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(UserViewSet, self).destroy(request, *args, **kwargs)


def login(request):
    id = request.POST['user_id']
    pwd = request.POST['user_pwd']
    msg = 0
    # 认证账户密码是否匹配
    user = None
    try:
        user = User.objects.get(id=id)
        if pwd == user.pwd:
            msg = 2
            request.session['user_id'] = user.id
            request.session['user_pwd'] = user.pwd
        else:
            msg = 1
    except:
        msg = -1

    # 管理员用户集合
    # admin_set = set()
    # 权限集合
    perm_set = set()

    # 将权限和管理员信息加入session
    try:
        duties = User.objects.get_user_duty(user)
        for duty in duties:
            # admin_set.add(duty.duty)
            perms = duty.duty.get_all_permissions()
            for perm in perms:
                perm_set.add(perm)

        # request.session['admin_set'] = list(admin_set)
        request.session['perm_set'] = list(perm_set)
    except:
        msg = -1

    # 检查用户是否为空，若是，需要修改信息
    if user.sex is None or \
        user.birthday is None or \
        user.political_choices is None or \
        user.political is None or \
        user.native_place is None or \
        user.id_number is None or \
        user.phone_number is None or \
        user.country_and_region is None:
        msg = 10

    ret = {
        "msg": msg
    }
    return HttpResponse(json.dumps(ret))


def logout(request):
    id = request.POST['user_id']
    msg = 0
    try:
        user = User.objects.get(id=id)
        request.session['user_id'] = None
        request.session['user_pwd'] = None
        request.session['admin_set'] = None
        request.session['perm_set'] = None
        msg = 1
    except:
        pass
    ret = {
        "msg": msg
    }
    return HttpResponse(json.dumps(ret))
