from django.db import models
from .User import User
from .Teacher import Teacher


class Major_Manager(models.Manager):
    def get_major_from_student(self, student):
        """
        获取学生专业
        :param student: 学生对象
        :return: Major
        """
        if isinstance(student, Undergraduate_Student):
            return student.student_class.grade.major
        elif isinstance(student, Graduate_Student):
            return student.student_class.grade.major
        else:
            return None


class Major(models.Model):
    name = models.CharField(max_length=30, verbose_name='专业', primary_key=True)
    objects = Major_Manager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业列表'
        permissions = (
            ('view_major', '可以查看专业'),
            ('create_major', '可以增加专业'),
            ('update_major', '可以修改专业'),
            ('delete_major', '可以删除专业'),
        )


class Student_Grade_Manager(models.Manager):
    pass


class Student_Grade(models.Model):
    name = models.CharField(verbose_name='年级', max_length=30)
    major = models.ForeignKey(Major, verbose_name='专业', on_delete=models.CASCADE)
    objects = Student_Grade_Manager()

    def __str__(self):
        return str(self.major) + str(self.name)

    class Meta:
        unique_together = ('name', 'major')
        verbose_name = '年级'
        verbose_name_plural = '年级列表'
        permissions = (
            ('view_grade', '可以查看年级'),
            ('create_grade', '可以增加年级'),
            ('update_grade', '可以修改年级'),
            ('delete_grade', '可以删除年级'),
        )


class Student_Class_Manager(models.Manager):
    pass


class Student_Class(models.Model):
    name = models.CharField(verbose_name='班级', max_length=30)
    grade = models.ForeignKey(Student_Grade, verbose_name='年级', on_delete=models.DO_NOTHING)
    headmaster = models.ForeignKey(Teacher, verbose_name='班导师', on_delete=models.DO_NOTHING, related_name='headmaster_teacher')
    instructor = models.ForeignKey(Teacher, verbose_name='辅导员', on_delete=models.DO_NOTHING, related_name='instructor_teacher')
    objects = Student_Class_Manager()

    def __str__(self):
        return str(self.grade) + str('-') + str(self.name)

    class Meta:
        unique_together = ('name', 'grade')
        verbose_name = '班级'
        verbose_name_plural = '班级列表'
        permissions = (
            ('view_class', '可以查看班级'),
            ('create_class', '可以增加班级'),
            ('update_class', '可以修改班级'),
            ('delete_class', '可以删除班级'),
        )


class Undergraduate_Student_Manager(models.Manager):
    pass


class Undergraduate_Student(models.Model):
    user = models.ForeignKey(User, verbose_name='本科生用户', on_delete=models.CASCADE, primary_key=True)
    student_class = models.ForeignKey(Student_Class, verbose_name='班级', on_delete=models.DO_NOTHING, null=True, blank=True)
    objects = Undergraduate_Student_Manager()

    def __str__(self):
        return str(self.user)

    def get_major(self):
        return self.student_class.grade.major

    class Meta:
        verbose_name = '本科生'
        verbose_name_plural = '本科生列表'


class Graduate_Student(models.Model):
    user = models.ForeignKey(User, verbose_name='研究生用户', on_delete=models.CASCADE, primary_key=True)
    student_class = models.ForeignKey(Student_Class, verbose_name='班级', on_delete=models.DO_NOTHING, null=True, blank=True)
    instructor = models.ForeignKey(Teacher, verbose_name='导师', on_delete=models.CASCADE, null=True, blank=True)
    on_the_job = models.BooleanField(verbose_name='是否在职')
    company = models.CharField(verbose_name='工作单位', max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_major(self):
        return self.student_class.grade.major

    class Meta:
        verbose_name = '研究生'
        verbose_name_plural = '研究生列表'


