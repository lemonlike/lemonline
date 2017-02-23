# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import CourseOrg, CityDict, Teacher
from .forms import UserAskForm
from operation.models import UserFavorite
from courses.models import Course
# Create your views here.


class OrgView(View):
    def get(self,request):
        # 课程机构
        all_org = CourseOrg.objects.all()
        hot_org = all_org.order_by("-click_nums")[:3]
        # 城市
        all_city = CityDict.objects.all()

        # 机构搜索功能
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_org = all_org.filter(name__icontains=search_keywords)

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
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:2]
        current_page = "home"
        return render(request, "org-detail-homepage.html", {
            "all_courses": all_courses,
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgCourseView(View):
    """
    机构课程列表页
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()
        current_page = "course"
        return render(request, "org-detail-course.html", {
            "all_courses": all_courses,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgDescView(View):
    """
    机构介绍页
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        current_page = "desc"
        return render(request, "org-detail-desc.html", {
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class OrgTeacherView(View):
    """
    机构讲师页
    """
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_teachers = course_org.teacher_set.all()
        current_page = "teacher"
        return render(request, "org-detail-teachers.html", {
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,
        })


class AddFavView(View):
    """
    用户收藏和取消收藏
    """
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            # 判断用户登陆状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type="application/json")

        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 如果记录存在，则表示用户取消收藏
            exist_records.delete()
            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type="application/json")
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type="application/json")
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type="application/json")


class TeacherListView(View):
    """
    课程讲师列表页
    """
    def get(self, request):
        all_teachers = Teacher.objects.all()

        # 机构搜索功能
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_teachers = all_teachers.filter(name__icontains=search_keywords)

        # 讲师按热度排序
        sort = request.GET.get("sort", "")
        if sort == "hot":
            all_teachers = all_teachers.order_by("-click_nums")

        # 讲师排行榜
        sort_teachers = all_teachers.order_by("-click_nums")[:3]

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_teachers, 3, request=request)
        teacher = p.page(page)
        return render(request, "teachers-list.html", {
            "all_teachers": teacher,
            "sort_teachers": sort_teachers,
            "sort": sort,
        })


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))

        # 课程点击数自增
        teacher.click_nums += 1
        teacher.save()

        has_teacher_faved = False
        if UserFavorite.objects.filter(user=request.user, fav_id=teacher.id, fav_type=3):
            has_teacher_faved =True

        has_org_faved = False
        if UserFavorite.objects.filter(user=request.user, fav_id=teacher.org_id, fav_type=2):
            has_org_faved = True

        # 讲师排行榜
        sort_teachers = Teacher.objects.all().order_by("-click_nums")[:3]

        # 讲师所有课程
        all_courses = Course.objects.filter(teacher=teacher)
        return render(request, "teacher-detail.html", {
            "teacher": teacher,
            "sort_teachers": sort_teachers,
            "all_courses": all_courses,
            "has_teacher_faved": has_teacher_faved,
            "has_org_faved": has_org_faved,
        })