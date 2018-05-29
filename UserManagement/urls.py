from django.urls import path
from UserManagement.views import user_view
urlpatterns = [
    path('login/', user_view.login, name='login'),
    path('logout/', user_view.logout, name='logout'),
]
