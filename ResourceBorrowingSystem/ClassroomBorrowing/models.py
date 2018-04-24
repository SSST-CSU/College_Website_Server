from django.db import models
from UserManagement.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class RoomBorrowingApply(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.room) + str('@') + str(self.user)


class RoomBorrowingRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.room) + str('@') + str(self.user)
