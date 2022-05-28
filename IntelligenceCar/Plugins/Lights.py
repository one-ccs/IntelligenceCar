#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Lights.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Devices.LEDBoard import LEDBoard

class Lights():
    """led 车灯"""

    def __init__(self, left_pin, right_pin):
        self.lights = None

        if left_pin and right_pin:
            self.lights = LEDBoard(left_pin, right_pin, pwm=True)

    def set(self, left_brightness=1.0, right_brightness=1.0):
        """同时调节两个 led 的亮度, 取值为 0.0 熄灭到 1.0 高亮。"""
        self.lights.value = (left_brightness, right_brightness)

    def both_on(self):
        self.lights.on()

    def both_off(self):
        self.lights.off()
        