from django.urls import path

from .index_views import *
from .user_center_views import *
from .articles_views import *


app_name = 'Pages'

urlpatterns = [
    path('', index),
    path('index/', index),

    path('usercenter/', user_center),
    path('usercenter/articles/', user_center_articles),
    path('usercenter/home/', user_center_home),
    path('usercenter/users/', user_center_users),
    path('usercenter/pages/', user_center_pages),
    path('usercenter/meetingroom/', user_center_meetingroom),

    path('article/id/<int:id>/', article_page),
    path('article/id/<slug>/', article_page),
]
