# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/23 15:26'

from django.conf.urls import url

from .views import UserInfoView, ImageUploadView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MycourseView, \
    MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView

urlpatterns = [
    # 用户基本信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),

    # 用户上传头像
    url(r'^image/upload/$', ImageUploadView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    # 个人中心发送修改邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 个人中心修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 个人中心我的课程
    url(r'^my_course/$', MycourseView.as_view(), name="my_course"),

    # 我收藏的机构
    url(r'^fav/org/$', MyFavOrgView.as_view(), name="fav_org"),

    # 我收藏的讲师
    url(r'^fav/teacher/$', MyFavTeacherView.as_view(), name="fav_teacher"),

    # 我收藏的课程
    url(r'^fav/course/$', MyFavCourseView.as_view(), name="fav_course"),

    # 我收藏的课程
    url(r'^my_message/$', MyMessageView.as_view(), name="my_message"),
]