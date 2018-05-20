from django.urls import path

from .index_views import *

urlpatterns = [
    path('', index),
    path('index/', index),
]
