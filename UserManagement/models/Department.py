from django.db import models


class Department(models.Model):
    name = models.CharField('部门', max_length=30)
    superior = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上级部门')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门列表'
