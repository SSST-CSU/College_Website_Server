from django.urls import path

from .index_views import *
from .user_center_views import *
from .articles_views import *


app_name = 'Pages'

urlpatterns = [
    path('', index),
    path('index/', index),
    path('usercenter/', user_center),
    path('article/id/<int:id>/', article_page),
    path('article/id/<slug>/', article_page),
]
