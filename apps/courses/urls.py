# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/19 16:01'

from django.conf.urls import url

from .views import CourseListView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name="list"),
]