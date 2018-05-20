from django.db import models
from .Major import Major


class Student_Grade(models.Model):
    name = models.CharField(verbose_name='年级', max_length=30)
    major = models.ForeignKey(Major, verbose_name='专业', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.major) + str(self.name)

    class Meta:
        unique_together = ('name', 'major')
        verbose_name = '年级'
        verbose_name_plural = '年级'
