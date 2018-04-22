from django.urls import path

from Pages.views import index

urlpatterns = [
    path('', index),
    path('index/', index),
]
