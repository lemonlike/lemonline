# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg,CityDict
# Create your views here.


class OrgView(View):
    def get(self,request):
        all_org = CourseOrg.objects.all()
        all_city = CityDict.objects.all()

        # 按照类别进行筛选
        category = request.GET.get('ct', "")
        if category:
            all_org = all_org.filter(category=category)

        # 按照城市对机构进行筛选
        city_id = request.GET.get('city', "")
        if city_id:
            all_org = all_org.filter(city_id=int(city_id))

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
        })