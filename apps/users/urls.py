# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/23 15:26'

from django.conf.urls import url

from .views import UserInfoView, ImageUploadView, UpdatePwdView

urlpatterns = [
    # 用户基本信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),

    # 用户上传头像
    url(r'^image/upload/$', ImageUploadView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

]