#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Servo.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import Adafruit_PCA9685

class Servo():
    """舵机"""

    def __init__(self, pin=None, frequency=50):
        self.pin = pin
        self._angle = 0

        if pin:
            self.servo = Adafruit_PCA9685.PCA9685()
            self.servo.set_pwm_freq(frequency)  # 设置 pwm 频率 (Hz)
            self.angle = 0

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        """设置舵机的角度"""
        self._angle = angle
        angle = 4096 * ((angle * 11) + 500) / 20000
        self.servo.set_pwm(self.pin, 0, int(angle))
