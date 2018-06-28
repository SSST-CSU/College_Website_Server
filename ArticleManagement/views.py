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

    def get_article_queryset(self, request, permission):
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

        # 获取权限信息
        permissions = article_permissions.filter(permission=permission)
        permissions = permissions | article_permissions.filter(permission='all')

        # 获取所有栏目
        for per in permissions:
            column = per.column
            queryset = queryset | Article.objects.get_column_articles(column)

        return queryset

    def list(self, request, *args, **kwargs):
        result = self.get_article_queryset(request, 'list')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArticleViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        result = self.get_article_queryset(request, 'create')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArticleViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        result = self.get_article_queryset(request, 'update')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArticleViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        result = self.get_article_queryset(request, 'destroy')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArticleViewSet, self).destroy(request, *args, **kwargs)


class ColumnViewSet(ModelViewSet):
    serializer_class = ColumnSerializer

    def get_column_queryset(self, request, permission):
        queryset = Column.objects.none()

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

        # 获取权限信息
        permissions = article_permissions.filter(permission=permission)
        permissions = permissions | article_permissions.filter(permission='all')

        # 获取所有栏目
        for per in permissions:
            column = per.column
            queryset = queryset | Column.objects.filter(column=column)

        return queryset

    def list(self, request, *args, **kwargs):
        result = self.get_column_queryset(request, 'list')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ColumnViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        result = self.get_column_queryset(request, 'create')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ColumnViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        result = self.get_column_queryset(request, 'update')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ColumnViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        result = self.get_column_queryset(request, 'destroy')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ColumnViewSet, self).destroy(request, *args, **kwargs)


class ArchivalArticlesViewSet(ModelViewSet):
    serializer_class = ArchivalArticlesSerializer

    def get_archival_article_queryset(self, request, permission):
        queryset = ArchivalArticles.objects.none()

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

        # 获取权限信息
        permissions = article_permissions.filter(permission=permission)
        permissions = permissions | article_permissions.filter(permission='all')

        # 获取所有栏目
        for per in permissions:
            column = per.column
            queryset = queryset | ArchivalArticles.objects.filter(column=column)

        return queryset

    def list(self, request, *args, **kwargs):
        result = self.get_archival_article_queryset(request, 'list')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArchivalArticlesViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        result = self.get_archival_article_queryset(request, 'create')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArchivalArticlesViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        result = self.get_archival_article_queryset(request, 'update')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArchivalArticlesViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        result = self.get_archival_article_queryset(request, 'destroy')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArchivalArticlesViewSet, self).destroy(request, *args, **kwargs)


class ArticleStatViewSet(ModelViewSet):
    serializer_class = ArticleStatSerializer

    def get_article_stat_queryset(self, request, permission):
        queryset = ArticleStat.objects.none()

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

        # 获取权限信息
        permissions = article_permissions.filter(permission=permission)
        permissions = permissions | article_permissions.filter(permission='all')

        # 获取所有文章
        articles = Article.objects.none()
        for per in permissions:
            column = per.column
            articles = articles | Article.objects.get_column_articles(column)

        # 获取所有文章状态
        for article in articles:
            queryset = queryset | ArticleStat.objects.filter(article=article)

        return queryset

    def list(self, request, *args, **kwargs):
        result = self.get_article_stat_queryset(request, 'list')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArticleStatViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        result = self.get_article_stat_queryset(request, 'create')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArticleStatViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        result = self.get_article_stat_queryset(request, 'update')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArticleStatViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        result = self.get_article_stat_queryset(request, 'destroy')
        if isinstance(result, Response):
            return result
        else:
            self.queryset = result
            return super(ArticleStatViewSet, self).destroy(request, *args, **kwargs)


class ArticlePermissionViewSet(ModelViewSet):
    serializer_class = ArticlePermissionSerializer

    def list(self, request, *args, **kwargs):
        perm_set = request.session['perm_set']
        if 'ArticleManagement.view_articlepermission' in perm_set:
            return super(ArticlePermissionViewSet, self).list(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)