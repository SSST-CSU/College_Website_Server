from django.db import models
from .Permition import Permition
from .Duty import Duty


class Duty_Permition(models.Model):
    permition = models.ForeignKey(Permition, verbose_name='权限', on_delete=models.CASCADE)
    duty = models.ForeignKey(Duty, verbose_name='职务', on_delete=models.CASCADE)
    level = models.IntegerField(verbose_name='权限等级')

    def __str__(self):
        return str(self.duty) + str('-') + str(self.permition)

    class Meta:
        unique_together = ('permition', 'duty')
        verbose_name = '职务权限'
        verbose_name_plural = '职务权限对应表'