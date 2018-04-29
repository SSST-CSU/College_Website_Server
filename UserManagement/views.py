from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
# from rest_framework.decorators import action
from rest_framework import viewsets
# from UserManagement import models
from UserManagement.serializer import *

# Create your views here.


# 登录
class UserLoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = User.objects.get(username__exact=username)
        if user.password == password:
            serializer = UserSerializers(user)
            new_data = serializer.data
            # 记忆已登录用户
            self.request.session['user_id'] = user.id
            # 生成用户登录日志
            create = UserLoginLog.objects.create(user=user.id)
            return Response(new_data, status=HTTP_200_OK)
        return Response('password error', HTTP_400_BAD_REQUEST)


# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
#     permission_classes = (IsOwnerOrReadOnly)
#
#     def perform_create(self, serializer):
#         print(self.request.user)
#         serializer.save(owner=User.objects.get(id=self.request.session.get('user_id')))


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserLoginLogViewSet(viewsets.ModelViewSet):
    queryset = UserLoginLog.objects.all()
    serializer_class = UserLoginLogSerializers
