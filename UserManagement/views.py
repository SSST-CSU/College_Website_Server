from rest_framework.response import Response
# from rest_framework.decorators import action
from rest_framework import viewsets
from UserManagement.models import *
from UserManagement.serializer import *

# Create your views here.


class LoginViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializers
