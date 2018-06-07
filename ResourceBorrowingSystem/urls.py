from django.urls import path
from rest_framework.routers import DefaultRouter
from .ClassroomBorrowing.views import *

router = DefaultRouter()
router.register('Room', RoomViewSet)
router.register('RoomBorrowingApply', RoomBorrowingApplyViewSet)

app_name = 'ResourceBorrowingSystem'

urlpatterns = [

]

urlpatterns += router.urls