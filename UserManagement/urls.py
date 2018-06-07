from django.urls import path
from rest_framework.routers import DefaultRouter

from UserManagement.views import user_view, teacher_view, student_view


router = DefaultRouter()
router.register('user', user_view.UserViewSet)
router.register('teacher', teacher_view.TeacherViewSet)


app_name = 'UserManagement'

urlpatterns = [
    path('login/', user_view.login, name='login'),
    path('logout/', user_view.logout, name='logout'),
]

urlpatterns += router.urls
