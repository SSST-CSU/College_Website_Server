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
  
