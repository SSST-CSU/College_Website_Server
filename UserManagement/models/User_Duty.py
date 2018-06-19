from django.db import models
from django.contrib.auth.models import User as DutyUser
from .User import User


class User_Duty(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    duty = models.ForeignKey(DutyUser, verbose_name='职务', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.duty) + str('-') + str(self.user)

    class Meta:
        unique_together = ('user', 'duty')
        verbose_name = '用户职务'
        verbose_name_plural = '用户-职务对照表'