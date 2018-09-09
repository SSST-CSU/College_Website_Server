from django.db import models


# Create your models here.
class ApplyForm(models.Model):
    id = models.CharField(verbose_name='学号', max_length=10, primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=5)
    sex = models.BooleanField(verbose_name='性别', max_length=1, choices=((True, '男'), (False, '女')))
    political_choices = (
        (1, '中共党员'),
        (2, '中共预备党员'),
        (3, '共青团员'),
        (4, '民革党员'),
        (5, '民盟盟员'),
        (6, '民建会员'),
        (7, '民进会员'),
        (8, '农工党党员'),
        (9, '致公党党员'),
        (10, '九三学社社员'),
        (11, '台盟盟员'),
        (12, '无党派人士'),
        (13, '群众'),
    )
    political = models.IntegerField(verbose_name='政治面貌', max_length=10, choices=political_choices)
    # 籍贯
    place = models.CharField(verbose_name='籍贯', max_length=30)
    classes = models.CharField(verbose_name='班级', max_length=4)
    qq = models.CharField(verbose_name='QQ', max_length=15)
    tel = models.CharField(verbose_name='电话', max_length=20)
    swap = models.BooleanField('服从调剂')
    first = models.CharField('第一志愿', max_length=8)
    second = models.CharField('第二志愿', max_length=8, null=True, blank=True)
    # 本人获奖情况及特长、技能等
    award = models.TextField('获奖技能与特长', max_length=500, null=True, blank=True)
    # 对学生机构干部工作的想法
    think = models.TextField('学生机构干部工作的想法', max_length=500, null=True, blank=True)
    # 对学院发展及对学生工作的建议
    advice = models.TextField('学院发展及对学生工作的建议', max_length=500, null=True, blank=True)
    # 备注
    attach = models.TextField('备注', max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.id) + "-" + str(self.name)

    class Meta:
        verbose_name = '申请'
        verbose_name_plural = '申请'


class Question(models.Model):
    id = models.CharField(primary_key=True, max_length=5)  # 有可能是中文，例如：竞赛部
    q = models.TextField(max_length=500, null=False)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'


def upload_to(instance, filename):
    """
    自定义附件上传路径
    :param instance: 对象
    :param filename: 文件名
    :return: 文件路径
    """
    from django.conf import settings
    import time
    return '/'.join(
        [settings.MEDIA_ROOT, str(instance.apply), time.strftime('%Y-%m-%d', time.localtime(time.time())), filename])


class Answer(models.Model):
    apply = models.ForeignKey(ApplyForm, verbose_name='申请', on_delete=models.CASCADE, null=False)
    ques = models.ForeignKey(Question, verbose_name='问题', on_delete=models.CASCADE, null=False)
    ans = models.TextField(verbose_name='回答', max_length=1200)
    enclosure = models.FileField(verbose_name='附件', upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "回答"
        verbose_name_plural = "回答"


class Task(models.Model):
    start_time = models.DateTimeField('开始时间')
    end_time = models.DateTimeField('结束时间')
    name = models.CharField('考核名称', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "考核"
        verbose_name_plural = "考核"


class Task_Question(models.Model):
    task = models.ForeignKey(Task)
    question = models.Model(Question)

    def __str__(self):
        return str(self.task) + "-" + str(self.question)

    class Meta:
        verbose_name = "考核-问题"
        verbose_name_plural = "考核-问题"


class Interview(models.Model):
    time = models.DateTimeField('时间')
    place = models.CharField('地点', max_length=20)

    def __str__(self):
        return str(self.time) + "@" + str(self.place)

    class Meta:
        verbose_name = "面试"
        verbose_name_plural = "面试"
