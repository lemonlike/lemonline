# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-17 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '\u57f9\u8bad\u673a\u6784'), ('gx', '\u9ad8\u6821'), ('gr', '\u4e2a\u4eba')], default='pxjg', max_length=10, verbose_name='\u673a\u6784\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='logo'),
        ),
    ]
