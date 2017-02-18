# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg,CityDict
from .forms import UserAskForm
# Create your views here.


class OrgView(View):
    def get(self,request):
        # 课程机构
        all_org = CourseOrg.objects.all()
        hot_org = all_org.order_by("-click_nums")[:3]
        # 城市
        all_city = CityDict.objects.all()

        # 按照类别进行筛选
        category = request.GET.get('ct', "")
        if category:
            all_org = all_org.filter(category=category)

        # 按照城市对机构进行筛选
        city_id = request.GET.get('city', "")
        if city_id:
            all_org = all_org.filter(city_id=int(city_id))

        # 按学习人数或课程数排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_org = all_org.order_by("-students")
        elif sort == "courses":
            all_org = all_org.order_by("-course_nums")

        all_nums = all_org.count()

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_org, 5, request=request)
        org = p.page(page)

        return render(request, "org-list.html", {
            "all_org": org,
            "all_city": all_city,
            "all_nums": all_nums,
            "city_id": city_id,
            "category": category,
            "hot_org": hot_org,
            "sort": sort,
        })


class AddUserAskView(View):
    # 用户添加咨询
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type="application/json")


class OrgHomeView(View):
    """
    机构首页
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:2]
        return render(request, "org-detail-homepage.html", {
            "all_courses": all_courses,
            "all_teachers": all_teachers,
        })