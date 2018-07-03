from django.urls import path

from Pages.views.index import *
from Pages.views.user_center import *
from Pages.views.user_center_articles import *
from Pages.views.articles import *


app_name = 'Pages'

urlpatterns = [
    path('', index),
    path('index/', index),
    path('login/', login_page),

    path('usercenter/', user_center),
    path('usercenter/articles/', user_center_articles),
    path('usercenter/articles/edit/', user_center_articles_edit),
    path('usercenter/articles/edit/id/<int:id>/', user_center_articles_edit_id),

    path('usercenter/home/', user_center_home),
    path('usercenter/users/', user_center_users),
    path('usercenter/pages/', user_center_pages),
    path('usercenter/meetingroom/', user_center_meetingroom),

    path('article/id/<int:id>/', article_page),
    path('article/name/<str:name>/', article_page),

    path('column/id/<int:id>/', columns_page),
]
