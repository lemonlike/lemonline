# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/18 15:27'

from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
