# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-04 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soil', '0003_auto_20171001_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoilMoisture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(null=True)),
                ('suitable_crop', models.CharField(max_length=400, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]