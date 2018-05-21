from django.urls import path

from .index_views import *
from .user_center_views import *

urlpatterns = [
    path('', index),
    path('index/', index),
    path('usercenter/', user_center)
]
