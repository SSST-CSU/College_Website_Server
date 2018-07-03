# College Website Server
中南大学软件学院院网。网站使用Django-2.0编写，请使用python3.6及以上版本运行。  


## 目录结构
- [**ArticleManagement**](ArticleManagement/README.md)
- [**OnlineJudgeSystem**](OnlineJudgeSystem/README.md)
- [**Pages**](Pages/READEME.md)
- [**ResourceBorrowinSystem**](ResourceBorrowingSystem/README.md)
- [**SchoolOfSoftware**](SchoolOfSoftware/README.md)
- **templates**
    - **htmls**
    - **static**
        - admin
        - css
        - fonts
        - images
        - js
        - rest_framework
- [**UserManagerment**](UserManagement/README.md)
- db.sqlite3
- manage.py

## 部署与运行
```
sudo apt-get install python-pip
pip install django
pip install djangorestframework
pip install django-jinja
pip install django-filter

git clone github.com/pzf0000/College_Website_Server.git
cd College_Website_Server

python manage.py makemigration
python manage.py migrate
python manage.py createsuperuser
```
注意：已配置好超级管理员`root` ，其密码是 admin123，可以不用重复配置，若需要清空数据，请删除数据库，重新做ORM迁移。

