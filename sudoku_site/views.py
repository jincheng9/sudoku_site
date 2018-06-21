# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    """
    website homepage
    :param request:
    :return:
    """
    return render(request, 'index.html')