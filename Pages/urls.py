from django.urls import path

from .index_views import *
from .user_center_views import *


app_name = 'Pages'

urlpatterns = [
    path('', index),
    path('index/', index),
    path('usercenter/', user_center)
]
