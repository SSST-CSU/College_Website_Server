from django.db import models
from ArticleManagement.models import Column


class NavbarObject(models.Model):
    """
    导航栏显示设置（不包含登陆后显示的栏目）
    """
    page_name = models.CharField(verbose_name='页面名称', max_length=30, default="index")
    serial_number = models.FloatField(verbose_name='序号')
    name = models.CharField('名称', max_length=25)
    herf = models.CharField('相对路径', max_length=100, null=True, blank=True)
    superior = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上级栏目')

    class Meta:
        unique_together = ('page_name', 'serial_number')
        verbose_name = '导航栏内容'
        verbose_name_plural = '导航栏内容'

    def __str__(self):
        return str(self.page_name) + str(self.serial_number) + str('-') + str(self.name)


class DisplayImage(models.Model):
    """
    展示的图片
    """
    page_name = models.CharField(verbose_name='页面名称', max_length=30, default="index")
    serial_number = models.IntegerField(verbose_name='序号')
    name = models.CharField('名称', max_length=25)
    herf = models.CharField('相对路径', max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.page_name) + str('img') + str(self.serial_number)

    class Meta:
        unique_together = ('page_name', 'serial_number')
        verbose_name = '页面图片轮播'
        verbose_name_plural = '页面图片轮播'


class DisplayColumn(models.Model):
    """
    展示的栏目
    """
    page_name = models.CharField(verbose_name='页面名称', max_length=30, default="index")
    serial_number = models.IntegerField(verbose_name='序号')
    column = models.ForeignKey(Column, verbose_name='栏目', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.page_name) + str('col') + str(self.serial_number) + str('-') + str(self.column)

    class Meta:
        unique_together = ('page_name', 'serial_number')
        verbose_name = '页面显示栏目'
        verbose_name_plural = '页面显示栏目'


class Page_Type(models.Model):
    """
    页面的状态，需要展示二级主页的时候使用
    0 为与首页相同板式
    """
    page_name = models.CharField(verbose_name='页面名称', max_length=30, primary_key=True)
    type = models.IntegerField()

    def __str__(self):
        return str(self.page_name) + str('-') + str(type)

    class Meta:
        verbose_name = '页面显示状态'
        verbose_name_plural = '页面显示状态'
