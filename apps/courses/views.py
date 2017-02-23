# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Course, CourseResource
from operation.models import UserFavorite, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin


# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        # 课程搜索功能
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))

        # 按热度或参与人数排序
        sort = request.GET.get("sort", "")
        if sort == "hot":
            all_courses = all_courses.order_by("-click_nums")
        elif sort == "students":
            all_courses = all_courses.order_by("-students")

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)
        courses = p.page(page)
        return render(request, "course-list.html", {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 课程点击数自增
        course.click_nums += 1
        course.save()

        # 相关课程推荐
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:2]
        else:
            relate_courses = []

        # 传递收藏的值
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            elif UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        return render(request, "course-detail.html", {
            "course": course,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
        })


class LessonView(LoginRequiredMixin, View):
    """
    章节详情页
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 查询用户是否已经关联了该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        # 学过该课程的人还学过哪些课程

        user_courses = UserCourse.objects.filter(course=course)
        # 取到学习过该课程的人的所有id
        user_ids = [user_course.user.id for user_course in user_courses]
        # 取到学习过该课程人还学习过的课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        course_ids = [user_course.course.id for user_course in all_user_courses]
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]

        all_resource = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html", {
            "course": course,
            "course_resources": all_resource,
            "relate_courses": relate_courses,
        })


class CommentsView(LoginRequiredMixin, View):
    """
    课程评论页
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 学过该课程的人还学过哪些课程

        user_courses = UserCourse.objects.filter(course=course)
        # 取到学习过该课程的人的所有id
        user_ids = [user_course.user.id for user_course in user_courses]
        # 取到学习过该课程人还学习过的课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        course_ids = [user_course.course.id for user_course in all_user_courses]
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]

        all_resource = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.filter(course=course).order_by("-add_time")
        return render(request, "course-comment.html", {
            "course": course,
            "course_resources": all_resource,
            "course_comments": all_comments,
            "relate_courses": relate_courses,
        })


class AddCommentsView(View):
    """
    用户添加评论
    """

    def post(self, request):
        if not request.user.is_authenticated():
            # 判断用户登陆状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type="application/json")

        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if course_id > 0 and comments:
            course_comment = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comment.user = request.user
            course_comment.course = course
            course_comment.comments = comments
            course_comment.save()
            return HttpResponse('{"status":"success", "msg":"评论成功"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail", "msg":"评论失败"}', content_type="application/json")
