from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

import json


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        queryset = Article.objects.none()

        # 获取登录信息
        try:
            my_id = request.session['user_id']
            me = User.objects.get(id=my_id)
        except:
            data = {'detail': '未登录'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        # 获取职务信息
        user_duties = User.objects.get_user_duty(me)
        article_permissions = ArticlePermission.objects.none()
        for duty in user_duties:
            article_permissions = article_permissions | ArticlePermission.objects.filter(duty=duty.duty)

        # 获取所有list权限信息
        permissions = article_permissions.filter(permission='list')
        permissions = permissions | article_permissions.filter(permission='all')

        # 获取所有栏目
        for per in permissions:
            column = per.column
            queryset = queryset | Article.objects.get_column_articles(column)

        self.queryset = queryset
        return super(ArticleViewSet, self).list(request, *args, **kwargs)