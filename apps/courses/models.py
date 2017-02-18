# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from organization.models import CourseOrg
# Create your models here.


class Course(models.Model):
    name = models.CharField(verbose_name=u"课程名", max_length=50)
    desc = models.CharField(verbose_name=u"课程描述", max_length=300)
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(verbose_name=u"课程等级", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    learn_time = models.IntegerField(verbose_name=u"学习时长(分钟数)", default=0)
    students = models.IntegerField(verbose_name=u"学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name=u"收藏人数", default=0)
    image = models.ImageField(verbose_name=u"封面图", upload_to="courses/%Y/%m", max_length=100)
    click_nums = models.IntegerField(verbose_name=u"点击量", default=0)
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(verbose_name="章节名", max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(verbose_name=u"视频名", max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(verbose_name=u"课程资源", max_length=100)
    download = models.FileField(verbose_name=u"资源文件", upload_to="courses/resource/%Y/%m", max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name
