# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-01 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soil', '0002_auto_20171001_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='land_profile_id',
            field=models.IntegerField(null=True),
        ),
    ]