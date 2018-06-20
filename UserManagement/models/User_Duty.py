from django.db import models
from django.contrib.auth.models import User as DutyUser


class UserDutyManager(models.Manager):
    pass


class User_Duty(models.Model):
    from .User import User
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    duty = models.ForeignKey(DutyUser, verbose_name='职务', on_delete=models.CASCADE)
    objects = UserDutyManager()

    def __str__(self):
        return str(self.duty) + str('-') + str(self.user)

    class Meta:
        unique_together = ('user', 'duty')
        verbose_name = '用户职务'
        verbose_name_plural = '用户-职务对照表'
        permissions = (
            ('view_user_duties', '可以查看用户职务'),
            ('create_user_duty', '可以创建用户职务'),
            ('update_user_duties', '可以修改用户职务'),
            ('delete_user_duties', '可以删除用户职务'),
        )
