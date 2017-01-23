# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 03:30
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170122_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='标题')),
                ('body', ckeditor.fields.RichTextField(verbose_name='正文')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '关于这里',
                'verbose_name': '关于这里',
            },
        ),
    ]