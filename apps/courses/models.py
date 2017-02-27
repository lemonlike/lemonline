# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

from organization.models import CourseOrg, Teacher
# Create your models here.


class Course(models.Model):
    name = models.CharField(verbose_name=u"课程名", max_length=50)
    desc = models.CharField(verbose_name=u"课程描述", max_length=300)
    detail = UEditorField(verbose_name=u"课程详情", width=600, height=300, imagePath="courses/ueditor/",
                         filePath="courses/ueditor/", default='')
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师", null=True, blank=True)
    degree = models.CharField(verbose_name=u"课程等级", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    learn_time = models.IntegerField(verbose_name=u"学习时长(分钟数)", default=0)
    students = models.IntegerField(verbose_name=u"学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name=u"收藏人数", default=0)
    image = models.ImageField(verbose_name=u"封面图", upload_to="courses/%Y/%m", max_length=100)
    click_nums = models.IntegerField(verbose_name=u"点击量", default=0)
    category = models.CharField(verbose_name=u"课程类别", max_length=20, default=u"后端开发")
    tag = models.CharField(verbose_name=u"课程标签", max_length=10, default="")
    need_know = models.CharField(verbose_name=u"课程须知", max_length=300, default="")
    teacher_tell = models.CharField(verbose_name=u"老师告诉你", max_length=300, default="")
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_lesson_nums(self):
        # 获取章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        # 获取学习用户
        return self.usercourse_set.all()

    def get_course_lesson(self):
        # 获取课程章节
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(verbose_name="章节名", max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        # 获取章节视频
        return self.video_set.all()

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(verbose_name=u"视频名", max_length=100)
    url = models.CharField(verbose_name=u"访问地址", max_length=100, default="")
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

    def __unicode__(self):
        return self.name
