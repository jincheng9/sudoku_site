# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import traceback
from contest import models

# Create your views here.
def page(request):
    """
    大赛报名页面
    :param request:
    :return:
    """
    return render(request, 'contest.html')


def apply(request):
    """
    报名注册方法, 前端传POST请求过来
    :param request:
    :return:
    """
    try:
        apply_info = request.POST
        name = apply_info.get('name', None)
        sex = apply_info.get('sex', None)
        mobile_phone = apply_info.get('mobile', None)
        company = apply_info.get('company', None)
        age = apply_info.get('age', None)
        if name is None or sex is None or mobile_phone is None or company is None or age is None:
            return HttpResponse("报名信息未填写完整！")
        else:
            applicant = models.Applicant(name=name, sex=sex, mobile_phone = mobile_phone, company=company, age=age)
            applicant.save()
            return HttpResponse("报名成功")
    except:
        print traceback.format_exc()