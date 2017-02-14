# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/14 20:46'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)