# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from scripts import serial_ports
from time import sleep
import serial


def index(request):
    return render(request, 'soil/index.html')


def analyze(request):
    print "Serial ports are : ", serial_ports()
    context_dict = {'serial_ports': serial_ports()}
    return render(request, 'soil/analyze.html', context_dict)


def analyze_sample(request, port):
    # ser = serial.Serial(port, 9600)  # Establish the connection on a specific port
    ser = serial.Serial(
        port=port,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    # RxTx
    ser.isOpen()
    while 1:
        out = ''
        while ser.inWaiting() > 0:
            out += ser.read(1)
        if out != '':
            print ">>Received String: %s" % out
        result = []
    for i in range(0, 10):
        # result.append(int(ser.readline()))
        sleep(0.1)
    print result # Read the newest output from the Arduino
    context_dict = {'result': result}
    return render(request, 'soil/analysis-result.html', context_dict)

