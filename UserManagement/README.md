# 用户管理系统
这是负责用户认证的App
## Start 
你需要安装django-cas-sso:  
```
pip install django-cas-sso
```
`django-cas-sso` 已经在`setting.py` 中的`MIDDLEWARE_CLASSES` 进行了设置，无需重复设置。  
如果使用Django-2.0，有可能需要修改`django-cas-sso` 的源代码，或者你需要选择Django-2.0的分支进行安装。  
如果对Django-sso有任何疑问，可以 [访问页面](https://pypi.org/project/django-cas-sso/).  
  
