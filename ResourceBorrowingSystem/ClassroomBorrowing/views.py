from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from .serializers import *


# Create your views here.
class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomBorrowingApplyViewSet(ModelViewSet):
    serializer_class = RoomBorrowingApplySerializer
    queryset = RoomBorrowingApply.objects.all()


class RoomBorrowingRecordViewSet(ModelViewSet):
    serializer_class = RoomBorrowingRecordSerializer
    queryset = RoomBorrowingRecord.objects.all()
