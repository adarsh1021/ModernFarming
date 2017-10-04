# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from scripts import serial_ports, get_values
from models import *
from time import sleep
import serial


def index(request):
    return render(request, 'soil/index.html')


def analyze(request):
    print "Serial ports are : ", serial_ports()
    context_dict = {'serial_ports': serial_ports()}
    return render(request, 'soil/analyze.html', context_dict)


def analyze_sample(request, port):
    result = get_values(port)
    percent = 0.0
    for r in result[1:]:
        percent += float(r)
    result = percent/30.0
    context_dict = {'result': result}

    all_crops = Crops.objects.all()
    calibrate = SoilMoisture.objects.get(suitable_crop='CALIBRATION').percent
    suitable_crops = []
    for crop in all_crops:
        if result >= calibrate-crop.moisture_factor and result <= calibrate+crop.moisture_factor:
            suitable_crops.append(crop.crop)

    context_dict['suitable_crops']= suitable_crops
    print "lower", calibrate-crop.moisture_factor
    return render(request, 'soil/analysis-result.html', context_dict)


def analyze_save(request, result):
    return render(request, 'soil/save.html')


def calibrate(request):
    context_dict = {'serial_ports': serial_ports()}
    return render(request, 'soil/calibrate.html', context_dict)


def calibrate_sample(request, port):
    result = get_values(port)
    percent = 0.0
    for r in result[1:]:
        percent += float(r)
    context_dict = {'result': percent / 30.0}  # ignoring first read because its causing error
    return render(request, 'soil/calibration-result.html', context_dict)


def calibrate_save(request, result):
    c = SoilMoisture.objects.get(suitable_crop='CALIBRATION')
    c.percent = float(result)
    c.save()
    return render(request, 'soil/save.html')


def analysis_save(request, result):
    c = SoilMoisture()
    c.percent = float(result)
    c.save()
    return render(request, 'soil/save.html')


def analysis_history(request):
    samples = SoilMoisture.objects.all().order_by('-time').exclude(suitable_crop='CALIBRATION')
    context_dict = {'samples': samples}
    return render(request, 'soil/analysis-history.html', context_dict)