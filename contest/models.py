# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    age = models.FloatField()
