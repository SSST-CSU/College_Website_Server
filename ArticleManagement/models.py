from django.db import models

from UserManagement.models.User import User


class ArticleManager(models.Manager):
    pass


class Article(models.Model):
    """
    一篇文章
    """
    id = models.IntegerField(verbose_name='文章编号', primary_key=True)
    edit_time = models.DateTimeField(verbose_name='修改时间')  # 第一次创建的时间也是这个
    title = models.CharField(verbose_name='标题', max_length=30)
    author = models.CharField(verbose_name='作者', max_length=30)
    editor = models.CharField(verbose_name='编辑', max_length=30)
    content = models.TextField(verbose_name='内容', max_length=100000)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='创建者', null=True, blank=True)
    objects = ArticleManager()

    def __str__(self):
        return str(self.title)

    class Meta:
        # 为版本管理，一个文章有多个版本记录，但id相同，按标题获取时应该返回时间最晚的那个
        unique_together = ('id', 'edit_time', 'title')
        verbose_name = '文章'
        verbose_name_plural = '文章'


class ColumnManager(models.Manager):
    pass


class Column(models.Model):
    """
    栏目
    """
    name = models.CharField('栏目名称', primary_key=True, max_length=30)
    superior = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='上级栏目', null=True, blank=True)
    objects = ColumnManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'


class ArchivalArticlesManager(models.Manager):
    pass


class ArchivalArticles(models.Model):
    """
    存档的文章，即已存入栏目的
    """
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    column = models.ForeignKey(Column, verbose_name='栏目', on_delete=models.CASCADE)
    objects = ArchivalArticlesManager()

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
    stat_choices = (
        (0, '暂存'),
        (1, '发布'),
    )
    stat = models.IntegerField(choices=stat_choices, default=1)

    def __str__(self):
        return str(self.article) + str('-') + str(self.stat)

    class Meta:
        verbose_name = '文章的状态'
        verbose_name_plural = '文章的状态'


class ArticlePermissionManager(models.Manager):
    pass


class ArticlePermission(models.Model):
    """
    用户文章栏目权限
    按照栏目给不同职务权限
    每个用户自身都有权限修改或删除自己创建的文章
    获得栏目权限后将会自动获得子栏目的所有权限，无法按照单个文章进行权限赋予
    """

    from django.contrib.auth.models import User as DutyUser

    duty = models.ForeignKey(DutyUser, verbose_name='职务', on_delete=models.CASCADE)
    column = models.ForeignKey(Column, verbose_name='栏目', on_delete=models.CASCADE)
    permission_choices = (
        ('all', '全部权限'),
        ('list', '可以查看'),
        ('create', '可以增加'),
        ('update', '可以修改'),
        ('destroy', '可以删除'),
    )
    permission = models.CharField(verbose_name='权限名称', choices=permission_choices, max_length=10)
    objects = ArticlePermissionManager()

    class Meta:
        unique_together = ('duty', 'column', 'permission')
        verbose_name = '职务栏目权限'
        verbose_name_plural = '用户职务-栏目权限表'
