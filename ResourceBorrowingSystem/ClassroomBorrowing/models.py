from django.db import models
from UserManagement.models.User import User


class Room(models.Model):
    name = models.CharField('名称', max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '教室/会议室'
        verbose_name_plural = '教室/会议室'


class RoomBorrowingApply(models.Model):
    user = models.ForeignKey(User, verbose_name='申请人', on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, verbose_name='申请教室', on_delete=models.DO_NOTHING)
    apply_time = models.DateTimeField('申请提交时间')
    start_time = models.DateTimeField('申请开始时间')
    end_time = models.DateTimeField('申请结束时间')
    stat = models.CharField('申请状态', max_length=30)

    def __str__(self):
        return str(self.room) + str('@') + str(self.user)

    class Meta:
        verbose_name = '教室/会议室借用申请'
        verbose_name_plural = '教室/会议室借用申请'
