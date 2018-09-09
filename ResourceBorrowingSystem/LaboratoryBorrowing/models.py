from django.db import models
from UserManagement.models.User import User


class Laboratory(models.Model):
    name = models.CharField('实验室名称', max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "实验室"
        verbose_name_plural = "实验室"


class LaboratoryApplyReason(models.Model):
    reason = models.CharField('申请类型',  max_length=20)

    def __str__(self):
        return str(self.reason)

    class Meta:
        verbose_name = "实验室申请理由"
        verbose_name_plural = "实验室申请理由"


class LaboratoryBorrowingApplyManager(models.Manager):
    def get_apply_by_user(self, user):
        """
        返回最近的一次申请
        :param user:
        :return:
        """
        all_apply = self.filter(user=user).order_by('update_time').reverse()
        if all_apply.count() == 0:
            return None
        return all_apply.first()

    def get_all_apply_by_user(self, user):
        all_apply = self.filter(user=user).order_by('update_time').reverse()
        if all_apply.count() == 0:
            return None
        id_set = set()
        for apply in all_apply:
            if apply.apply_id in id_set:
                all_apply = all_apply.exclude(apply_id=apply.apply_id, stat=apply.stat)
            else:
                id_set.add(apply.apply_id)
        return all_apply

    def get_apply_by_id(self, id):
        return self.filter(apply_id=id).order_by('update_time').reverse()


def upload_to(instance, filename):
    """
    自定义附件上传路径
    :param instance: 对象
    :param filename: 文件名
    :return: 文件路径
    """
    from django.conf import settings
    import time
    return '/'.join([settings.MEDIA_ROOT, str(instance.user), time.strftime('%Y-%m-%d',time.localtime(time.time())), filename])


class LaboratoryBorrowingApply(models.Model):
    apply_id = models.CharField(verbose_name="申请编号", max_length=25)
    user = models.ForeignKey(User, verbose_name="申请人", on_delete=models.DO_NOTHING)
    room = models.CharField(verbose_name='申请实验室', max_length=20)
    apply_time = models.DateTimeField('申请提交时间')
    update_time = models.DateTimeField('申请变更时间')
    reason_type = models.CharField('申请类型', max_length=20)
    reason = models.TextField('申请理由', max_length=500, blank=True, null=True)
    start_time = models.DateTimeField('申请开始时间')
    end_time = models.DateTimeField('申请结束时间')
    stat_choices = (
        ('已保存', '已保存'),
        ('已提交', '已提交'),
        ('审核中', '审核中'),
        ('排序中', '排序中'),
        ('申请通过', '申请通过'),
        ('申请不通过', '申请不通过')
    )
    stat = models.CharField('申请状态', max_length=30, choices=stat_choices)
    proof_document = models.FileField('附件', upload_to=upload_to, null=True, blank=True)
    seat_number = models.IntegerField('座位号', null=True, blank=True)
    content = models.CharField('备注', max_length=50, null=True, blank=True)
    registration_number = models.IntegerField('注册编号', null=True, blank=True)
    objects = LaboratoryBorrowingApplyManager()

    def __str__(self):
        return str(self.update_time) + str('-') + str(self.room) + str('@') + str(self.user)

    class Meta:
        unique_together = ('apply_id', 'stat')
        verbose_name = "实验室借用申请"
        verbose_name_plural = "实验室借用申请"


class AdminUser(models.Model):
    from django.contrib.auth.models import User as Duty
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE, verbose_name='职务')
    laboratory = models.CharField(verbose_name='实验室', max_length=20)

    class Meta:
        verbose_name = '实验室管理员'
        verbose_name_plural = '实验室管理员'


class ApplyUserGrade(models.Model):
    from UserManagement.models.Student import Student_Grade
    grade = models.ForeignKey(Student_Grade, on_delete=models.CASCADE, verbose_name='年级')

    class Meta:
        verbose_name = '可申请年级'
        verbose_name_plural = '可申请年级'
