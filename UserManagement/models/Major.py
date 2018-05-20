from django.db import models


class Major(models.Model):
    name = models.CharField(max_length=30, verbose_name='专业', primary_key=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业'
