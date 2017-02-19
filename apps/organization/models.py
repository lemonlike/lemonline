# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.


class CityDict(models.Model):
    name = models.CharField(verbose_name=u"城市名称", max_length=20)
    desc = models.CharField(verbose_name=u"描述", max_length=200)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(verbose_name=u"机构名称", max_length=50)
    category = models.CharField(verbose_name=u"机构类别", choices=(("pxjg", u"培训机构"), ("gx", u"高校"), ("gr", u"个人")), max_length=10, default="pxjg")
    desc = models.TextField(verbose_name=u"机构描述")
    click_nums = models.IntegerField(verbose_name=u"点击量", default=0)
    fav_nums = models.IntegerField(verbose_name=u"收藏数", default=0)
    students = models.IntegerField(verbose_name=u"学习人数", default=0)
    course_nums = models.IntegerField(verbose_name=u"课程数", default=0)
    image = models.ImageField(verbose_name=u"logo", upload_to="org/%Y/%m", max_length=100)
    address = models.CharField(verbose_name=u"机构地址", max_length=150)
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(verbose_name=u"教师名", max_length=20)
    image = models.ImageField(verbose_name=u"头像", upload_to="teacher/%Y/m", max_length=100, default='')
    work_years = models.IntegerField(verbose_name=u"工作年限", default=0)
    work_company = models.CharField(verbose_name=u"就职公司", max_length=50)
    work_position = models.CharField(verbose_name=u"公司职位", max_length=50)
    points = models.CharField(verbose_name=u"教学特点", max_length=50)
    click_nums = models.IntegerField(verbose_name=u"点击量", default=0)
    fav_nums = models.IntegerField(verbose_name=u"收藏数", default=0)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
