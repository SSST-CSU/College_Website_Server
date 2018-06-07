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
        duty = request.user
        if duty.has_perm('UserManagement.view_all_users'):
            return super(UserViewSet, self).list(request, *args, **kwargs)
        elif duty.has_perm('UserManagement.view_my_users'):
            self.queryset = User.objects.get_my_users()
            return super(UserViewSet, self).list(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        duty = request.user
        if duty.has_perm('UserManagement.create_user'):
            return super(UserViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        duty = request.user
        if duty.has_perm('UserManagement.update_all_users'):
            return super(UserViewSet, self).update(request, *args, **kwargs)
        elif duty.has_perm('UserManagement.update_my_users'):
            self.queryset = User.objects.get_my_users()
            return super(UserViewSet, self).update(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        duty = request.user
        if duty.has_perm('UserManagement.delete_all_users'):
            return super(UserViewSet, self).destroy(request, *args, **kwargs)
        elif duty.has_perm('UserManagement.delete_my_users'):
            self.queryset = User.objects.get_my_users()
            return super(UserViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


def login(request):
    id = request.POST['user_id']
    pwd = request.POST['user_pwd']
    msg = 0
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
        msg = 1
    except:
        pass
    ret = {
        "msg": msg
    }
    return HttpResponse(json.dumps(ret))
