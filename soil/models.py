# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    email = models.CharField(max_length=200, null=True, blank=True)
    land_profile_id = models.IntegerField(null=True)


class LandProfile(models.Model):
    size = models.FloatField(max_length=10, null=True)
    state = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    relative_humidity = models.FloatField(max_length=3, null=True) # in percent


class SoilMoisture(models.Model):
    user = models.IntegerField(null=True)
    percent = models.FloatField(null=True)
    suitable_crop = models.CharField(max_length=400, null=True)
    time = models.DateTimeField(auto_now_add=True)


class Crops(models.Model):
    crop = models.CharField(max_length=200, null=True)
    moisture_factor = models.FloatField(null=True)
