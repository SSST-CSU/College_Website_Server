from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.


class LaboratoryViewSet(ModelViewSet):
    serializer_class = LaboratorySerializer
    queryset = Laboratory.objects.all()


class LaboratoryApplyReasonViewSet(ModelViewSet):
    serializer_class = LaboratoryApplyReasonSerializer
    queryset = LaboratoryApplyReason.objects.all()


# class LaboratoryBorrowingApplyViewSet(ModelViewSet):
#     serializer_class = LaboratoryBorrowingApply
#     queryset = LaboratoryBorrowingApply.objects.all()
