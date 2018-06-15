from django.db import models


class Article(models.Model):
    """
    一篇文章
    """
    creation_time = models.DateTimeField('创建时间')
    title = models.CharField('标题', max_length=30)
    author = models.CharField('作者', max_length=30)
    editor = models.CharField('编辑', max_length=30)
    content = models.TextField('内容')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Column(models.Model):
    """
    栏目
    """
    name = models.CharField('栏目名称', primary_key=True, max_length=30)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'


class ArchivalArticles(models.Model):
    """
    存档的文章，即已存入栏目的
    """
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    column = models.ForeignKey(Column, verbose_name='栏目', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.article) + str('-') + str(self.column)

    class Meta:
        unique_together = ('article', 'column')
        verbose_name = '文章的栏目'
        verbose_name_plural = '文章的栏目'


class ArticleStat(models.Model):
    """
    文章状态
    """
    article = models.OneToOneField(Article, verbose_name='文章', on_delete=models.CASCADE, primary_key=True)
    stat = models.CharField(max_length=30)

    def __str__(self):
        return str(self.article) + str('-') + str(self.stat)

    class Meta:
        verbose_name = '文章是状态'
        verbose_name_plural = '文章的状态'
