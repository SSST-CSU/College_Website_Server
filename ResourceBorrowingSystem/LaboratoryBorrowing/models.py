from django.db import models
from UserManagement.models.User import User


class Laboratory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "实验室"
        verbose_name_plural = "实验室"


class ApplyReason(models.Model):
    reason = models.CharField(max_length=20)

    def __str__(self):
        return str(self.reason)

    class Meta:
        verbose_name = "申请理由"
        verbose_name_plural = "申请理由"


class LaboratoryBorrowingApplyManager(models.Manager):
    def get_apply_by_user(self, user):
        all_apply = self.filter(user=user).order_by('update_time').reverse()
        if all_apply.count() == 0:
            return None
        return all_apply.first()

    def get_all_apply_by_user(self, user):
        return self.filter(user=user).order_by('update_time').reverse()

    def get_apply_by_id(self, id):
        return self.filter(id=id).order_by('update_time').reverse()


class LaboratoryBorrowingApply(models.Model):
    id = models.IntegerField("申请编号")
    user = models.ForeignKey(User, verbose_name="申请人", on_delete=models.DO_NOTHING)
    room = models.CharField(verbose_name='申请实验室', max_length=20)
    apply_time = models.DateTimeField('申请提交时间')
    update_time = models.DateTimeField('申请变更时间')
    reason_type = models.CharField('申请类型', max_length=20)
    reason = models.TextField('申请理由', max_length=500)
    start_time = models.DateTimeField('申请开始时间')
    end_time = models.DateTimeField('申请结束时间')
    stat = models.CharField('申请状态', max_length=30)
    object = LaboratoryBorrowingApplyManager()

    def __str__(self):
        return str(self.room) + str('@') + str(self.user)

    class Meta:
        unique_together = ('id', 'stat')
        verbose_name = "实验室借用申请"
        verbose_name_plural = "实验室借用申请"
