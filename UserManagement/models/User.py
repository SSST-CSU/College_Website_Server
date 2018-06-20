from django.db import models
from .User_Duty import User_Duty
from .Student import Undergraduate_Student, Graduate_Student, Student_Class, Student_Grade
from .Teacher import Teacher


class User_Manager(models.Manager):
    def get_permissions_list(self):
        """
        返回权限列表
        :return: list
        """
        duties = self.get_duty()
        permissions = []
        for duty in duties:
            dutyuser = duty.duty
            for permission in dutyuser.get_all_permissions():
                permissions.append(permission)
        return permissions

    def get_my_users(self, user=None):
        """
        返回自己创建的所有用户
        :return: queryset<User>
        """
        if user is not None:
            return self.filter(creator=user)
        return self.filter(creator=self)

    def get_user_duty(self):
        """
        返回用户职务，若没有职务则为空
        :return: queryset<User_Duty>
        """
        return User_Duty.objects.filter(user=self)

    def get_class_users(self, user, instructor=False, headmaster=False):
        """
        返回自己班级的所有用户
        :return: queryset<User>
        """
        if isinstance(user, Undergraduate_Student):
            return self.filter(student_class=user.student_class)
        elif isinstance(user, Graduate_Student):
            return self.filter(student_class=user.student_class)
        elif isinstance(user, Teacher):
            result = self.none()
            # 辅导员
            if instructor:
                result = result | self.filter()
            # 班导师
            if headmaster:
                result = result | self.filter()
            return result
        else:
            return self.none()

    def get_grade_users(self, user, instructor=False, headmaster=False):
        """
        返回自己年级的所有用户
        :param user:
        :return: queryset<User>
        """
        result = self.none()
        if isinstance(user, Undergraduate_Student) or isinstance(user, Graduate_Student):
            student_grade = user.student_class.grade
            student_classes = Student_Class.objects.filter(grade=student_grade)
            for student_class in student_classes:
                result = result | self.filter(student_class=student_class)
        elif isinstance(user, Teacher):
            result = self.none()
            # 辅导员
            if instructor:
                result = result | self.filter()
            # 班导师
            if headmaster:
                result = result | self.filter()
        return result

    def get_teacher_gs(self, user):
        """
        返回同一个导师的用户
        :return: queryset<gs>
        """
        if isinstance(user, User):
            try:
                user = Graduate_Student.objects.get(id=user.id)
            except:
                return None
        if isinstance(user, Graduate_Student):
            return self.filter(instructor=user.instructor)
        elif isinstance(user, Teacher):
            return self.filter(instructor=user)

    def get_department_user(self, user):
        """
        获取同一部门的人员
        :return:queryset<User>
        """
        # todo


class User(models.Model):
    id = models.CharField(verbose_name='学工号', max_length=12, primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=10)
    pwd = models.CharField(verbose_name='密码', max_length=25)
    stat = models.BooleanField(verbose_name='用户状态', default=True)  # 0 不可用 1 可用
    name_used_before = models.CharField(verbose_name='曾用名', max_length=10, null=True, blank=True)
    sex = models.IntegerField(verbose_name='性别', max_length=1, choices=((0, '男'), (1, '女')))
    birthday = models.DateField(verbose_name='出生日期')
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
    political = models.IntegerField(verbose_name='政治面貌', choices=political_choices)
    native_place = models.CharField(verbose_name='籍贯', max_length=5)
    id_number = models.CharField(verbose_name='身份证号', max_length=20)
    phone_number = models.CharField(verbose_name='电话', max_length=20)
    country_and_region_choices = (
        ('AD', 'AD安道尔'),
        ('AE', 'AE阿联酋'),
        ('AF', 'AF阿富汗'),
        ('AG', 'AG安提瓜和巴布达'),
        ('AI', 'AI安圭拉'),
        ('AL', 'AL阿尔巴尼亚'),
        ('AM', 'AM亚美尼亚'),
        ('AO', 'AO安哥拉'),
        ('AR', 'AR阿根廷'),
        ('AT', 'AT奥地利'),
        ('AU', 'AU澳大利亚'),
        ('AW', 'AW阿鲁巴'),
        ('AZ', 'AZ阿塞拜疆'),
        ('BA', 'BA波黑'),
        ('BB', 'BB巴巴多斯'),
        ('BD', 'BD孟加拉'),
        ('BE', 'BE比利时'),
        ('BF', 'BF布基纳法索'),
        ('BG', 'BG保加利亚'),
        ('BH', 'BH巴林'),
        ('BI', 'BI布隆迪'),
        ('BJ', 'BJ贝宁'),
        ('BM', 'BM百慕大'),
        ('BN', 'BN文莱'),
        ('BO', 'BO玻利维亚'),
        ('BR', 'BR巴西'),
        ('BS', 'BS巴哈马'),
        ('BT', 'BT不丹'),
        ('BV', 'BV挪威布韦岛'),
        ('BW', 'BW博茨瓦纳'),
        ('BY', 'BY白俄罗斯'),
        ('BZ', 'BZ伯利兹'),
        ('CA', 'CA加拿大'),
        ('CF', 'CF中非共和国'),
        ('CG', 'CG刚果'),
        ('CH', 'CH瑞士'),
        ('CI', 'CI科特迪瓦'),
        ('CK', 'CK库克群岛'),
        ('CL', 'CL智利'),
        ('CM', 'CM喀麦隆'),
        ('CN', 'CN中国'),
        ('CO', 'CO哥伦比亚'),
        ('CR', 'CR哥斯达黎加'),
        ('CU', 'CU古巴'),
        ('CV', 'CV佛得角'),
        ('CX', 'CX澳大利亚圣诞岛'),
        ('CY', 'CY塞浦路斯'),
        ('CZ', 'CZ捷克共和国'),
        ('DE', 'DE德国'),
        ('DJ', 'DJ吉布提'),
        ('DK', 'DK丹麦'),
        ('DM', 'DM多明哥'),
        ('DO', 'DO多米尼加'),
        ('DZ', 'DZ阿尔及利亚'),
        ('EC', 'EC厄瓜多尔'),
        ('EE', 'EE爱沙尼亚'),
        ('EG', 'EG埃及'),
        ('EH', 'EH西撒哈拉'),
        ('ES', 'ES西班牙'),
        ('ET', 'ET埃塞俄比亚'),
        ('FI', 'FI芬兰'),
        ('FJ', 'FJ斐济'),
        ('FK', 'FK福克兰群岛'),
        ('FM', 'FM密克罗尼西亚'),
        ('FR', 'FR法国'),
        ('GA', 'GA加蓬'),
        ('GB', 'GB英国'),
        ('GD', 'GD格林纳达'),
        ('GE', 'GE格鲁吉亚'),
        ('GF', 'GF法属圭亚那'),
        ('GH', 'GH加纳'),
        ('GI', 'GI直布罗陀'),
        ('GL', 'GL格陵兰'),
        ('GM', 'GM冈比亚'),
        ('GN', 'GN几内亚'),
        ('GP', 'GP瓜德罗普'),
        ('GQ', 'GQ赤道几内亚'),
        ('GR', 'GR希腊'),
        ('GT', 'GT危地马拉'),
        ('GU', 'GU关岛'),
        ('GW', 'GW几内亚比绍'),
        ('GY', 'GY圭亚那'),
        ('HK', 'HK中国香港'),
        ('HN', 'HN洪都拉斯'),
        ('HR', 'HR克罗地亚'),
        ('HT', 'HT海地'),
        ('HU', 'HU匈牙利'),
        ('ID', 'ID印度尼西亚'),
        ('IE', 'IE爱尔兰'),
        ('IL', 'IL以色列'),
        ('IN', 'IN印度'),
        ('IQ', 'IQ伊拉克'),
        ('IR', 'IR伊朗'),
        ('IS', 'IS冰岛'),
        ('IT', 'IT意大利'),
        ('JM', 'JM牙买加'),
        ('JO', 'JO约旦'),
        ('JP', 'JP日本'),
        ('KE', 'KE肯尼亚'),
        ('KG', 'KG吉尔吉斯斯坦'),
        ('KH', 'KH柬埔寨'),
        ('KI', 'KI基里巴斯'),
        ('KM', 'KM科摩罗'),
        ('KP', 'KP朝鲜'),
        ('KR', 'KR韩国'),
        ('KW', 'KW科威特'),
        ('KY', 'KY开曼群岛'),
        ('KZ', 'KZ哈萨克斯坦'),
        ('LA', 'LA老挝'),
        ('LB', 'LB黎巴嫩'),
        ('LC', 'LC圣卢西亚'),
        ('LI', 'LI列支敦士登'),
        ('LK', 'LK斯里兰卡'),
        ('LR', 'LR利比里亚'),
        ('LS', 'LS莱索托'),
        ('LT', 'LT立陶宛'),
        ('LU', 'LU卢森堡'),
        ('LV', 'LV拉托维亚'),
        ('LY', 'LY利比亚'),
        ('MA', 'MA摩洛哥'),
        ('MD', 'MD摩尔多瓦'),
        ('MG', 'MG马达加斯加'),
        ('MH', 'MH马绍尔群岛'),
        ('ML', 'ML马里'),
        ('MM', 'MM缅甸'),
        ('MN', 'MN蒙古'),
        ('MO', 'MO中国澳门'),
        ('MR', 'MR毛里塔尼亚'),
        ('MT', 'MT马耳他'),
        ('MU', 'MU毛里求斯'),
        ('MV', 'MV马尔代夫'),
        ('MW', 'MW马拉维'),
        ('MX', 'MX墨西哥'),
        ('MY', 'MY马来西亚'),
        ('MZ', 'MZ莫桑比克'),
        ('NA', 'NA纳米比亚'),
        ('NC', 'NC新喀里多尼亚'),
        ('NE', 'NE尼日尔'),
        ('NG', 'NG尼日利亚'),
        ('NI', 'NI尼加拉瓜'),
        ('NL', 'NL荷兰'),
        ('NO', 'NO挪威'),
        ('NP', 'NP尼泊尔'),
        ('NR', 'NR瑙鲁'),
        ('NU', 'NU纽埃'),
        ('NZ', 'NZ新西兰'),
        ('OM', 'OM阿曼'),
        ('PA', 'PA巴拿马'),
        ('PE', 'PE秘鲁'),
        ('PF', 'PF法属玻里尼西亚'),
        ('PG', 'PG巴布亚新几内亚'),
        ('PH', 'PH菲律宾'),
        ('PK', 'PK巴基斯坦'),
        ('PL', 'PL波兰'),
        ('PN', 'PN皮特开恩群岛'),
        ('PT', 'PT葡萄牙'),
        ('PW', 'PW帕劳'),
        ('PY', 'PY巴拉圭'),
        ('QA', 'QA卡塔尔'),
        ('RO', 'RO罗马尼亚'),
        ('RU', 'RU俄罗斯'),
        ('RW', 'RW卢旺达'),
        ('SA', 'SA沙特阿拉伯'),
        ('SB', 'SB所罗门群岛'),
        ('SC', 'SC塞舌尔'),
        ('SD', 'SD苏丹'),
        ('SE', 'SE瑞典'),
        ('SG', 'SG新加坡'),
        ('SH', 'SH圣赫勒那'),
        ('SI', 'SI斯洛文尼亚'),
        ('SK', 'SK斯洛伐克'),
        ('SL', 'SL塞拉利昂'),
        ('SM', 'SM圣马力诺'),
        ('SN', 'SN塞内加尔'),
        ('SO', 'SO索马里'),
        ('SR', 'SR苏里南'),
        ('ST', 'ST圣多美与普林西比'),
        ('SV', 'SV萨尔瓦多'),
        ('SY', 'SY叙利亚'),
        ('SZ', 'SZ斯威士兰'),
        ('TD', 'TD乍得'),
        ('TF', 'TF法属南方领土'),
        ('TG', 'TG多哥'),
        ('TH', 'TH泰国'),
        ('TJ', 'TJ塔吉克斯坦'),
        ('TK', 'TK托克劳'),
        ('TM', 'TM土库曼斯坦'),
        ('TN', 'TH突尼斯'),
        ('TO', 'TO汤加'),
        ('TP', 'TP东帝汶'),
        ('TR', 'TR土尔其'),
        ('TT', 'TT特立尼达和多巴哥'),
        ('TV', 'TV图瓦卢'),
        ('TW', 'TW中国台湾'),
        ('TZ', 'TZ坦桑尼亚'),
        ('UA', 'UA乌克兰'),
        ('UG', 'UG乌干达'),
        ('UK', 'UK英国'),
        ('US', 'US美国'),
        ('UY', 'UY乌拉圭'),
        ('UZ', 'UZ乌兹别克斯坦'),
        ('VA', 'VA梵蒂冈'),
        ('VE', 'VE委内瑞拉'),
        ('VN', 'VN越南'),
        ('WS', 'WS西萨摩亚'),
        ('YE', 'YE也门'),
        ('YU', 'YU南斯拉夫'),
        ('ZA', 'ZA南非'),
        ('ZM', 'ZM赞比亚'),
        ('ZR', 'ZR扎伊尔'),
        ('ZW', 'ZW津巴布韦'),
    )
    country_and_region = models.CharField(verbose_name='国家或地区', max_length=3, choices=country_and_region_choices,
                                          default='CN')
    creator = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='用户创建者')
    objects = User_Manager()

    def to_student(self):
        """
        返回student对象，如果不存在student，则为None
        :return: object<student>
        """
        result = None
        try:
            # 如果本科生
            result = Undergraduate_Student.objects.get(id=self.id)
        except:
            try:
                # 如果研究生
                result = Graduate_Student.objects.get(id=self.id)
            except:
                # 非学生用户，或学生用户非在籍
                pass
        return result

    def to_teacher(self):
        """
        返回teacher对象，如果不存在teacher，则为None
        :return:
        """
        result = None
        try:
            # 如果Tescher
            result = Teacher.objects.get(id=self.id)
        except:
            pass
        return result

    def get_user_class(self):
        """
        返回用户的班级，如果没有班级，则为None
        :return: object<student_class>
        """
        result = None
        try:
            # 如果本科生
            result = Undergraduate_Student.objects.get(id=self.id).student_class
        except:
            try:
                # 如果研究生
                result = Graduate_Student.objects.get(id=self.id).student_class
            except:
                # 非学生用户，或学生用户非在籍
                pass
        return result

    def __str__(self):
        return str(self.id) + str('-') + str(self.name)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'
        permissions = (
            ('view_my_users', '可以查看自己创建的用户'),
            ('view_class_users', '可以查看自己班级的用户'),
            ('view_grade_users', '可以查看自己年级的用户'),
            ('view_all_users', '可以查看所有用户'),

            ('create_user', '可以增加用户'),

            ('update_my_users', '可以修改自己创建的用户'),
            ('update_class_users', '可以修改自己班级的用户'),
            ('update_grade_users', '可以修改自己年级的用户'),
            ('update_all_users', '可以修改所有用户'),

            ('delete_my_users', '可以删除自己创建的用户'),
            ('delete_class_users', '可以删除自己班级的用户'),
            ('delete_grade_users', '可以删除自己年级的用户'),
            ('delete_all_users', '可以删除所有用户'),
        )
