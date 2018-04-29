from django.urls import path

from Pages.views import *

urlpatterns = [
    path('', index),
    path('index/', index),
]
