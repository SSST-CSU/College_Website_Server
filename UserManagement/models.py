from django.db import models


# 用户表
class User(models.Model):
    id = models.CharField(max_length=12, primary_key=True)  # 用户学号
    name = models.CharField(max_length=5)  # 用户姓名
    pwd = models.CharField(max_length=25)  # 用户密码

    def __str__(self):
        return str(self.id) + str('-') + str(self.name)


# 用户登录日志表
class UserLoginLog(models.Model):
    id = models.AutoField(primary_key=True)  # 日志编号：自动生成
    time = models.DateTimeField(auto_now=True)  # 时间：插入时生成
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联用户，级联删除
<<<<<<< HEAD

    def __str__(self):
        return str(self.time) + str(' ') + str(self.user.name)


# 权限表
class Permission(models.Model):
    name = models.CharField(max_length=10)  # 权限名称
    description = models.CharField(max_length=30)  # 权限描述

    def __str__(self):
        return str(self.name)


# 用户权限表
class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联用户
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)  # 关联权限

    def __str__(self):
        return str(self.user.name) + '-' + str(self.permission.name)
=======

    def __str__(self):
        return str(self.time) + ' ' + str(self.user.name)
>>>>>>> 9ec56b0552ed3ae9bb5351c316795c332c080acb
