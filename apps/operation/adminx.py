# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/13 20:09'

import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user__username', 'course__name', 'comments']
    list_filter = ['user__username', 'course__name', 'comments', 'add_time']


# class UserFavoriteAdmin(object):


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)