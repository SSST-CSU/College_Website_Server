from django.db import models


class User(models.Model):
    id = models.CharField('学号', max_length=12, primary_key=True)
    name = models.CharField('姓名', max_length=10)
    pwd = models.CharField('密码', max_length=25)

    def __str__(self):
        return str(self.id) + str('-') + str(self.name)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'


class Permition(models.Model):
    name = models.CharField('权限名称', primary_key=True, max_length=30)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = '权限列表'


class Department(models.Model):
    name = models.CharField('部门', max_length=30)
    superior = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上级部门')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门列表'


class Duty(models.Model):
    name = models.CharField('职务名称', max_length=30)
    department = models.ForeignKey(Department, verbose_name='部门', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.department) + str('-') + str(self.name)

    class Meta:
        unique_together = ('name', 'department')
        verbose_name = '职务'
        verbose_name_plural = '职务列表'


class Duty_Permition(models.Model):
    permition = models.ForeignKey(Permition, verbose_name='权限', on_delete=models.CASCADE)
    duty = models.ForeignKey(Duty, verbose_name='职务', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.duty) + str('-') + str(self.permition)

    class Meta:
        unique_together = ('permition', 'duty')
        verbose_name = '职务权限'
        verbose_name_plural = '职务权限对应表'


class User_Duty(models.Model):
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    duty = models.ForeignKey(Duty, verbose_name='职务', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.duty) + str('-') + str(self.user)

    class Meta:
        unique_together = ('user', 'duty')
        verbose_name = '用户职务'
        verbose_name_plural = '用户职务对应表'

