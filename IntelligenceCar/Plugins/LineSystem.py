#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  LineSystem.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Devices import LineSensor


class LineSystem():
    """三个巡线传感器组成的巡线系统"""

    def __init__(self, left_pin, mid_pin, right_pin):
        self.left = None
        self.mid = None
        self.right = None

        if left_pin:
            self.left = LineSensor(left_pin)
        if mid_pin:
            self.mid = LineSensor(mid_pin)
        if right_pin:
            self.right = LineSensor(right_pin)

    @property
    def state(self):
        """返回传感器状态"""
        return (self.left.value, self.mid.value, self.right)
