from django.db import models
from .Student_Grade import Student_Grade
from .Teacher import Teacher


class Student_Class(models.Model):
    name = models.CharField(verbose_name='班级', primary_key=True, max_length=30)
    grade = models.ForeignKey(Student_Grade, verbose_name='年级', on_delete=models.DO_NOTHING)
    headmaster = models.ForeignKey(Teacher, verbose_name='班导师', on_delete=models.DO_NOTHING, related_name='headmaster_teacher')
    instructor = models.ForeignKey(Teacher, verbose_name='辅导员', on_delete=models.DO_NOTHING, related_name='instructor_teacher')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'
