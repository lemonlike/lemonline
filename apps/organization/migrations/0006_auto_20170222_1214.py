# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-22 12:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20170222_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='need_know',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_tell',
        ),
    ]
