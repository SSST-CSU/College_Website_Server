from django.db import models
from .User import User
from .Student_Class import Student_Class
from .Teacher import Teacher


class Student(models.Model):
    user = models.ForeignKey(User, verbose_name='学生用户', on_delete=models.CASCADE, primary_key=True)
    student_class = models.ForeignKey(Student_Class, verbose_name='班级', on_delete=models.DO_NOTHING, null=True, blank=True)
    birthday = models.DateField(verbose_name='出生日期')
    instructor = models.ForeignKey(Teacher, verbose_name='导师', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'
