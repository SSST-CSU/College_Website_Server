from django.db import models


class User(models.Model):
    id = models.CharField('学工号', max_length=12, primary_key=True)
    name = models.CharField('姓名', max_length=10)
    pwd = models.CharField('密码', max_length=25)
    stat = models.CharField('用户状态', max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.id) + str('-') + str(self.name)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'