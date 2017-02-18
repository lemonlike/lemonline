# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/18 15:16'

from django.conf.urls import url, include

from .views import OrgView, AddUserAskView

# 课程机构列表页
urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name="list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
]