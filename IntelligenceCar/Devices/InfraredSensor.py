#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  InfraredSensor.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import RPi.GPIO as GPIO

class InfraredSensor():
    """红外避障传感器"""

    def __init__(self, pin=None):
        self.pin = pin

        if pin:
            GPIO.setwarnings(False)     # 关闭警告信息
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.IN)
        else:
            raise ValueError('初始化 class InfraredSensor 的参数 pin 为无效值。')

    @property
    def value(self):
        """返回传感器检测值。"""
        return GPIO.input(self.pin)
