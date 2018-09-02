from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('Room', RoomViewSet)
router.register('RoomBorrowingApply', RoomBorrowingApplyViewSet)

app_name = 'ResourceBorrowingSystem.ClassroomBorrowing'

urlpatterns = [

]

urlpatterns += router.urls