from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet

from ..models.User import User
from ..serializers.user_serializer import UserSerializer

import json


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.session.get('user_id') is not None

    def has_object_permission(self, request, view, blog):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return blog.owner.id == request.session.get('user_id')


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User


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
