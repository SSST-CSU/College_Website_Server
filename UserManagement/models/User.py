from django.db import models


class User_Manager(models.Manager):
    def get_my_users(self):
        """
        :return: 返回自己创建的所有用户
        """
        return self.all().filter(superior=self)


class User(models.Model):
    id = models.CharField('学工号', max_length=12, primary_key=True)
    name = models.CharField('姓名', max_length=10)
    pwd = models.CharField('密码', max_length=25)
    stat = models.CharField('用户状态', max_length=20, null=True, blank=True)
    creator = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='用户创建者')
    object = User_Manager()

    def __str__(self):
        return str(self.id) + str('-') + str(self.name)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'
        permissions = (
            ('view_my_users', '可以查看自己创建的用户'),
            ('view_all_users', '可以查看所有用户'),
            ('create_user', '可以增加用户'),
            ('update_my_users', '可以修改自己创建的用户'),
            ('update_all_users', '可以修改所有用户'),
            ('delete_my_users', '可以删除自己创建的用户'),
            ('delete_all_users', '可以删除所有用户'),
        )

