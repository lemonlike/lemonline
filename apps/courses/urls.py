# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/19 16:01'

from django.conf.urls import url

from .views import CourseListView, CourseDetailView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="list"),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="detail"),
]