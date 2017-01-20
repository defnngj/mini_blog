# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 07:24
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('img', models.CharField(default='/static/tx/default.jpg', max_length=200, verbose_name='头像地址')),
                ('intro', models.CharField(blank=True, max_length=200, null=True, verbose_name='简介')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('en_title', models.CharField(max_length=100, verbose_name='英文标题')),
                ('img', models.CharField(default='/static/img/article/default.jpg', max_length=200)),
                ('tags', models.CharField(blank=True, help_text='用逗号分隔', max_length=200, null=True, verbose_name='标签')),
                ('summary', models.TextField(verbose_name='摘要')),
                ('content', models.TextField(verbose_name='正文')),
                ('view_times', models.IntegerField(default=0)),
                ('zan_times', models.IntegerField(default=0)),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('pub_time', models.DateTimeField(default=False, verbose_name='发布时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '文章',
                'ordering': ['rank', '-is_top', '-pub_time', '-create_time'],
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='摘要')),
                ('img', models.CharField(default='/static/img/carousel/default.jpg', max_length=200, verbose_name='轮播图片')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='文章')),
            ],
            options={
                'verbose_name_plural': '轮播',
                'ordering': ['-create_time'],
                'verbose_name': '轮播',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='名称')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='上级分类')),
            ],
            options={
                'verbose_name_plural': '分类',
                'ordering': ['rank', '-create_time'],
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='专栏内容')),
                ('summary', models.TextField(verbose_name='专栏摘要')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ManyToManyField(to='blog.Article', verbose_name='文章')),
            ],
            options={
                'verbose_name_plural': '专栏',
                'ordering': ['-create_time'],
                'verbose_name': '专栏',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '评论',
                'ordering': ['-create_time'],
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='导航条内容')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='指向地址')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '导航条',
                'ordering': ['-create_time'],
                'verbose_name': '导航条',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类'),
        ),
    ]
