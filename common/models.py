# Create your models here.

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.db import models
from django.db.models import Count
from django.utils import timezone
from simplepro.components import fields as sfields
from django.apps import apps as dj_apps

class BaseModel(models.Model):
    created_at = sfields.DateTimeField(auto_now_add=True, verbose_name='创建时间', editable=True)
    updated_at = sfields.DateTimeField(auto_now=True, verbose_name='更新时间', editable=True)
    status = sfields.RadioField(choices=[(-1, '已删除'), (0, '禁用'), (1, '正常')], default=1, verbose_name='状态')

    # --------------------------------------------------------------------------
    def age_f(self):
        if hasattr(self, 'age'):
            if self.age < 0 or self.age is None:
                return '-'
            return self.age
        return 'error!'

    age_f.short_description = '年龄'
    age_f.admin_order_field = 'age'

    class Meta:
        abstract = True

    # 按月统计数据
    @classmethod
    def s_months_data(cls, l_m_r=None, column='created_at', top=None, top_key='count', where_map=None):
        f_map = {}
        if l_m_r is not None:
            s_month = timezone.datetime.now() + relativedelta(months=l_m_r[0])
            e_month = timezone.datetime.now() + relativedelta(months=l_m_r[1] + 1)

            # 当前时间
            start = timezone.datetime(year=s_month.year, month=s_month.month, day=1)
            end = timezone.datetime(year=e_month.year, month=e_month.month, day=1)
            f_map = {f"{column}__range": (start, end)}
        if where_map:
            f_map.update(where_map)
        res = cls.objects.filter(**f_map).extra(select={'year': f'year({column})', 'month': f'month({column})'}) \
            .values('year', 'month').annotate(count=Count(column)).order_by()
        res = sorted(res, key=lambda ele: f"{ele['year']}-{ele['month']:02d}")
        res = {f'{ele["year"]}-{ele["month"]:02d}': ele['count'] for ele in res}

        if l_m_r:
            # 补全所有月份
            for m in range(l_m_r[0], l_m_r[1] + 1):
                dd = timezone.datetime.now() + relativedelta(months=m)
                k = f"{dd.year}-{dd.month:02d}"
                v = 0
                if k in res:
                    continue
                res[k] = v

        # 补全top
        if top and top > len(res):
            _c = 1
            while top > len(res):
                dd = timezone.datetime.now() - relativedelta(months=_c)
                k = f"{dd.year}-{dd.month:02d}"
                v = 0
                _c += 1
                if k in res:
                    continue
                res[k] = v

        # 整形为list
        res = [{'date': k, 'data': {'count': v}} for k, v in res.items()]

        # 重新排序
        res = sorted(res, key=lambda ele: f"{ele['date']}")
        if top:
            if top_key:
                res = sorted(res, key=lambda ele: f"{ele['data'][top_key]}")
                res = list(reversed(res))
            res = res[:top]
        return res


class XJUser(AbstractUser, BaseModel):
    phone_num = models.CharField(max_length=20, blank=True, verbose_name='手机')
    company = models.CharField(max_length=200, blank=True, verbose_name='单位')
    groups = sfields.TransferField(
        Group,
        verbose_name='角色',
        blank=True,
        related_name="user_set",
        related_query_name="user",
        help_text='可以继承这个角色[/组]的所有权限',
        titles=['待选', '已选']
    )
    is_staff = models.BooleanField(
        '可登录后台',
        default=False,
        help_text='指明用户是否可以登录到这个管理站点。',
    )
    user_permissions = sfields.TransferField(
        Permission,
        verbose_name='权限',
        blank=True,
        help_text='这个用户的特定权限。 按住 Control 键或 Mac 上的 Command 键来选择多项。',
        related_name="user_set",
        related_query_name="user",
        titles=['待选', '已选']
    )

    class Meta:
        db_table = 'xjuser'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def user_group_display(self):
        if self.is_superuser:
            return '超级管理员'
        else:
            gps = Group.objects.filter(user=self)
            return ','.join([gp.name for gp in gps])

    user_group_display.short_description = '用户组'
