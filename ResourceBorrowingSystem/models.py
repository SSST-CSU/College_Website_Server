from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20)


class RoomBorrowingApply(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rba_room', primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class RoomBorrowingRecord(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rbr_room', primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
