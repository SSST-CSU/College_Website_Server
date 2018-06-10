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
    # permission_classes = (permissions.DjangoModelPermissions, )

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.view_all_users' in perm_set:
            return super(UserViewSet, self).list(request, *args, **kwargs)
        elif 'UserManagement.view_my_users' in perm_set:
            self.queryset = User.objects.get_my_users()
            return super(UserViewSet, self).list(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

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
        if 'UserManagement.update_all_users' in perm_set:
            return super(UserViewSet, self).update(request, *args, **kwargs)
        elif 'UserManagement.update_my_users' in perm_set:
            self.queryset = User.objects.get_my_users()
            return super(UserViewSet, self).update(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.delete_all_users' in perm_set:
            return super(UserViewSet, self).destroy(request, *args, **kwargs)
        elif 'UserManagement.delete_my_users' in perm_set:
            self.queryset = User.objects.get_my_users()
            return super(UserViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


def login(request):
    id = request.POST['user_id']
    pwd = request.POST['user_pwd']
    msg = 0
    # 认证账户密码是否匹配
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
    admin_set = set()
    # 权限集合
    perm_set = set()

    # 将权限和管理员信息加入session
    try:
        duties = User.objects.get_user_duty()
        for duty in duties:
            admin_set.add(duty.duty)
            perms = duty.duty.get_all_permissions()
            for perm in perms:
                perm_set.add(perm)
        request.session['admin_set'] = admin_set
        request.session['perm_set'] = perm_set
    except:
        msg = -1
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
