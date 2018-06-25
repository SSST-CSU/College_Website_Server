from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'ArticleManagement'

router = DefaultRouter()
router.register(prefix='article', viewset=ArticleViewSet, base_name='article')

urlpatterns = [

]

urlpatterns += router.urls
