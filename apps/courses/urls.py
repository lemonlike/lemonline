# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/19 16:01'

from django.conf.urls import url

from .views import CourseListView, CourseDetailView, LessonView, CommentsView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="list"),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="detail"),

    # 章节详情页
    url(r'^lesson/(?P<course_id>\d+)/$', LessonView.as_view(), name="lesson"),

    # 课程评论页
    url(r'^comments/(?P<course_id>\d+)/$', CommentsView.as_view(), name="comments"),
]