#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  InfraredSystem.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Devices.InfraredSensor import InfraredSensor

class InfraredSystem():
    """两个红外避障传感器组成的避障系统"""

    def __init__(self, left_pin=None, right_pin=None):
        self.left = None
        self.right = None

        if left_pin:
            self.left = InfraredSensor(left_pin)
        if right_pin:
            self.right = InfraredSensor(right_pin)
