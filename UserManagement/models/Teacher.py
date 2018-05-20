from django.db import models
from .User import *


class Teacher(models.Model):
    user = models.ForeignKey(User, verbose_name='教师用户', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '教师'
