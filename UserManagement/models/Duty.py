from django.db import models
from .Department import Department


class Duty(models.Model):
    name = models.CharField('职务名称', max_length=30)
    department = models.ForeignKey(Department, verbose_name='部门', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.department) + str('-') + str(self.name)

    class Meta:
        unique_together = ('name', 'department')
        verbose_name = '职务'
        verbose_name_plural = '职务列表'

