from django.db import models


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=5)
    pwd = models.CharField(max_length=25)

    def __str__(self):
        return str(self.id) + str('-') + str(self.name)
