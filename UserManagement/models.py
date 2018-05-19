from django.db import models


class User(models.Model):
    id = models.CharField('学工号', max_length=12, primary_key=True)
    name = models.CharField('姓名', max_length=10)
    pwd = models.CharField('密码', max_length=25)
    stat = models.CharField('用户状态', max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.id) + str('-') + str(self.name)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'


class Teacher(models.Model):
    user = models.ForeignKey(User, verbose_name='教师用户', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '教师'


class Major(models.Model):
    name = models.CharField(max_length=30, verbose_name='专业', primary_key=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业'


class Student_Grade(models.Model):
    name = models.CharField(verbose_name='年级', max_length=30)
    major = models.ForeignKey(Major, verbose_name='专业', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.major) + str(self.name)

    class Meta:
        unique_together = ('name', 'major')
        verbose_name = '年级'
        verbose_name_plural = '年级'


class Student_Class(models.Model):
    name = models.CharField(verbose_name='班级', primary_key=True, max_length=30)
    grade = models.ForeignKey(Student_Grade, verbose_name='年级', on_delete=models.DO_NOTHING)
    headmaster = models.ForeignKey(Teacher, verbose_name='班导师', on_delete=models.DO_NOTHING)
    instructor = models.ForeignKey(Teacher, verbose_name='辅导员', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'


class Student(models.Model):
    user = models.ForeignKey(User, verbose_name='学生用户', on_delete=models.CASCADE, primary_key=True)
    student_class = models.ForeignKey(Student_Class, verbose_name='班级', on_delete=models.DO_NOTHING, null=True, blank=True)
    birthday = models.DateField(verbose_name='出生日期')
    instructor = models.ForeignKey(Teacher, verbose_name='导师', on_delete=models.CASCADE, default=student_class.instructor.objects.first())

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'


class Permition_Manager(models.Manager):
    def get_root_permition(self):
        """
        获取权限树根节点，若有多棵树则返回多个节点
        :return: 所有的根节点
        """
        root = []
        for permition in self:
            if permition.superior is None:
                root.append(permition)
            elif not self.exists(permition.superior):
                root.append(permition)
        return root

    def get_sub_permition(self):
        """
        返回节点的所有子节点，若存在多个根节点，则存放在list中返回
        :return: 根节点的子节点
        """
        root = self.get_root_permition()
        sub_permitions = []
        for permition in root:
            sub_permitions.append(self.filter(superior=permition))
        return sub_permitions


class Permition(models.Model):
    name = models.CharField('权限名称', primary_key=True, max_length=30)
    superior = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上级权限')
    object = Permition_Manager()

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
    level = models.IntegerField(verbose_name='权限等级')

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
