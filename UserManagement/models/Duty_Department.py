from django.db import models
from django.contrib.auth.models import User as DutyUser
from .Department import Department


class Duty_Department(models.Model):
    duty = models.ForeignKey(DutyUser, on_delete=models.CASCADE, verbose_name='职务', max_length=30)
    department = models.ForeignKey(Department, verbose_name='部门', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.department) + str('-') + str(self.duty)

    class Meta:
        unique_together = ('duty', 'department')
        verbose_name = '职务'
        verbose_name_plural = '职务-部门对照表'

