# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/2/13 19:35'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'click_nums', 'fav_nums', 'address', 'city__name']
    list_filter = ['name', 'click_nums', 'fav_nums', 'address', 'city__name', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'add_time']
    search_fields = ['org__name', 'name', 'work_years', 'work_company', 'work_position']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)