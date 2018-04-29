# User Management System
Here is the django app which providing user authentication. 
## Start 
You need to execute the command to install django-cas-sso:  
```
pip install django-cas-sso
```
The `django-cas-sso` has been added in `MIDDLEWARE_CLASSES` of `setting.py`  
You must update `from django.urls import reverse` in the 10th line of `django_cas/middleware.py` if you are using django-2.0  
If you have any questions about the django sso, you can open the [page](https://pypi.org/project/django-cas-sso/).  
  
## 20180429
models.py中四个表：用户表、用户登录日志表、权限表（待改进）、用户权限表
views.py中：一个APIView（用户登录），两个viewset（用户信息、用户登录日志信息）
serializers.py中三个序列化类：用户、用户登录日志、权限
permissions.py尚未编写
