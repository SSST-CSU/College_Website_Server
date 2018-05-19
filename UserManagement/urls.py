from django.urls import path
from UserManagement.views import *
urlpatterns = [
    path('login/', login),
    path('logout/', logout),
]
