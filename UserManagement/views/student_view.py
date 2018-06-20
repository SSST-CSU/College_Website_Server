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
    serializer_class = MajorSerializer
    queryset = Major.objects.all()

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.view_majors' in perm_set:
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
        if 'UserManagement.update_majors' in perm_set:
            return super(MajorViewSet, self).update(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.delete_majors' in perm_set:
            return super(MajorViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class StudentGradeViewSet(ModelViewSet):
    serializer_class = StudentGradeSerializer
    queryset = Student_Grade.objects.all()

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.view_grade' in perm_set:
            return super(StudentGradeViewSet, self).list(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_grade' in perm_set:
            return super(StudentGradeViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.update_grade' in perm_set:
            return super(StudentGradeViewSet, self).update(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.delete_grade' in perm_set:
            return super(StudentGradeViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class StudentClassViewSet(ModelViewSet):
    serializer_class = StudentClassSerializer
    queryset = Student_Class.objects.all()

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.view_class' in perm_set:
            return super(StudentClassViewSet, self).list(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_class' in perm_set:
            return super(StudentClassViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.update_class' in perm_set:
            return super(StudentClassViewSet, self).update(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.delete_class' in perm_set:
            return super(StudentClassViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class UndergraduateStudentViewSet(UserViewSet):
    serializer_class = GraduateStudentSerializer

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        queryset = Graduate_Student.objects.none()
        perm = False

        if 'UserManagement.view_my_gs' in perm_set or 'UserManagement.view_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Graduate_Student.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.view_class_gs' in perm_set or 'UserManagement.view_class_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_class_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.view_grade_gs' in perm_set or 'UserManagement.view_grade_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_grade_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.view_all_gs' in perm_set or 'UserManagement.view_all_users' in perm_set:
            perm = True
            queryset = queryset | Graduate_Student.objects.all()

        if 'UserManagement.view_teacher_gs' in perm_set:
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Graduate_Student.objects.get_teacher_gs(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(UndergraduateStudentViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_us' in perm_set or 'UserManagement.create_user' in perm_set:
            return super(UndergraduateStudentViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        queryset = Undergraduate_Student.objects.none()
        perm = False

        if 'UserManagement.update_my_us' in perm_set or 'UserManagement.update_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Undergraduate_Student.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.update_class_us' in perm_set or 'UserManagement.update_class_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Undergraduate_Student.objects.get_class_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.update_grade_us' in perm_set or 'UserManagement.update_grade_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Undergraduate_Student.objects.get_grade_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.update_all_us' in perm_set or 'UserManagement.update_all_users' in perm_set:
            perm = True
            queryset = queryset | Undergraduate_Student.objects.all()

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(UndergraduateStudentViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        queryset = Undergraduate_Student.objects.none()
        perm = False

        if 'UserManagement.delete_my_us' in perm_set or 'UserManagement.delete_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Undergraduate_Student.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.delete_class_us' in perm_set or 'UserManagement.delete_class_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Undergraduate_Student.objects.get_class_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.delete_grade_us' in perm_set or 'UserManagement.delete_grade_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Undergraduate_Student.objects.get_grade_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.delete_all_us' in perm_set or 'UserManagement.delete_all_users' in perm_set:
            perm = True
            queryset = queryset | Undergraduate_Student.objects.all()

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(UndergraduateStudentViewSet, self).destroy(request, *args, **kwargs)


class GraduateStudentViewSet(UserViewSet):
    serializer_class = GraduateStudentSerializer

    def list(self, request, *args, **kwargs):
        """
        查看
        """
        perm_set = request.session['perm_set']
        queryset = Graduate_Student.objects.none()
        perm = False

        if 'UserManagement.view_my_gs' in perm_set or 'UserManagement.view_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Graduate_Student.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.view_class_gs' in perm_set or 'UserManagement.view_class_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_class_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.view_grade_gs' in perm_set or 'UserManagement.view_grade_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_grade_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.view_all_gs' in perm_set or 'UserManagement.view_all_users' in perm_set:
            perm = True
            queryset = queryset | Graduate_Student.objects.all()

        if 'UserManagement.view_teacher_gs' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_teacher_gs(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(GraduateStudentViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        增加
        """
        perm_set = request.session['perm_set']
        if 'UserManagement.create_gs' in perm_set or 'UserManagement.create_user' in perm_set:
            return super(GraduateStudentViewSet, self).create(request, *args, **kwargs)
        else:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        """
        修改
        """
        perm_set = request.session['perm_set']
        queryset = Graduate_Student.objects.none()
        perm = False

        if 'UserManagement.update_my_gs' in perm_set or 'UserManagement.update_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Graduate_Student.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.update_class_gs' in perm_set or 'UserManagement.update_class_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_class_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.update_grade_gs' in perm_set or 'UserManagement.update_grade_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_grade_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.update_all_gs' in perm_set or 'UserManagement.update_all_users' in perm_set:
            perm = True
            queryset = queryset | Graduate_Student.objects.all()

        if 'UserManagement.update_teacher_gs' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_teacher_gs(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(GraduateStudentViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除
        """
        perm_set = request.session['perm_set']
        queryset = Graduate_Student.objects.none()
        perm = False

        if 'UserManagement.delete_my_gs' in perm_set or 'UserManagement.delete_my_users' in perm_set:
            perm = True
            try:
                my_id = request.session['user_id']
                me = User.objects.get(id=my_id)
                queryset = queryset | Graduate_Student.objects.get_my_users(me)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)

        if 'UserManagement.delete_class_gs' in perm_set or 'UserManagement.delete_class_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_class_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.delete_grade_gs' in perm_set or 'UserManagement.delete_grade_users' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_grade_users(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if 'UserManagement.delete_all_gs' in perm_set or 'UserManagement.delete_all_users' in perm_set:
            perm = True
            queryset = queryset | Graduate_Student.objects.all()

        if 'UserManagement.delete_teacher_gs' in perm_set:
            try:
                user = User.objects.get(id=request.session['user_id'])
                queryset = queryset | Graduate_Student.objects.get_teacher_gs(user)
            except:
                data = {'detail': '未登录'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            perm = True

        if not perm:
            data = {'detail': '没有权限'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            self.queryset = queryset
            return super(GraduateStudentViewSet, self).destroy(request, *args, **kwargs)