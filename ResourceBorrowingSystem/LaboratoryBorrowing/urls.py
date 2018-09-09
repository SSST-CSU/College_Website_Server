from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'ResourceBorrowingSystem.LaboratoryBorrowing'

router = DefaultRouter()
router.register(prefix='laboratory', viewset=LaboratoryViewSet, base_name='laboratory')
router.register(prefix='laboratory_apply_reason', viewset=LaboratoryApplyReasonViewSet, base_name='laboratory_apply_reason')


urlpatterns = [
    path('apply_lab/', apply_lab),
    path('update_lab/', update_lab)
]

urlpatterns += router.urls