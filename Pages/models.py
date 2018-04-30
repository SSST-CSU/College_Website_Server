from django.db import models
from ArticleManagement.models import Column


class NavbarObject(models.Model):
    """
    导航栏显示设置（不包含登陆后的用户中心）
    """
    serial_number = models.FloatField('序号', primary_key=True)
    name = models.CharField('名称', max_length=25)
    herf = models.CharField('相对路径', max_length=100)

    class Meta:
        verbose_name = '导航栏内容'
        verbose_name_plural = '导航栏内容'

    def __str__(self):
        return str(self.serial_number) + str('-') + str(self.name)


class DisplayColumn(models.Model):
    """
    展示的栏目
    """
    serial_number = models.IntegerField('序号', primary_key=True)
    column = models.ForeignKey(Column, verbose_name='栏目', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.serial_number) + str('-') + str(self.column)

    class Meta:
        verbose_name = '主页显示栏目'
        verbose_name_plural = '主页显示栏目'
