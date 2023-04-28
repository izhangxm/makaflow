# Generated by Django 4.2 on 2023-04-28 04:37

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import simplepro.components.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='XJUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', simplepro.components.fields.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', simplepro.components.fields.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', simplepro.components.fields.RadioField(choices=[(-1, '已删除'), (0, '禁用'), (1, '正常')], default=1, verbose_name='状态')),
                ('phone_num', models.CharField(blank=True, max_length=20, verbose_name='手机')),
                ('company', models.CharField(blank=True, max_length=200, verbose_name='单位')),
                ('is_staff', models.BooleanField(default=False, help_text='指明用户是否可以登录到这个管理站点。', verbose_name='可登录后台')),
                ('groups', simplepro.components.fields.TransferField(blank=True, help_text='可以继承这个角色[/组]的所有权限', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='角色')),
                ('user_permissions', simplepro.components.fields.TransferField(blank=True, help_text='这个用户的特定权限。 按住 Control 键或 Mac 上的 Command 键来选择多项。', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='权限')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'xjuser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
