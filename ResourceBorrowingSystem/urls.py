from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'ResourceBorrowingSystem'

urlpatterns = [
    path('class/', include('ResourceBorrowingSystem.ClassroomBorrowing.urls')),
    path('equipment/', include('ResourceBorrowingSystem.EquipmentBorrowing.urls')),
    path('laboratory/', include('ResourceBorrowingSystem.LaboratoryBorrowing.urls')),
]
