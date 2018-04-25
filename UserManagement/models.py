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

    def __str__(self):
        return str(self.time) + ' ' + str(self.user.name)
