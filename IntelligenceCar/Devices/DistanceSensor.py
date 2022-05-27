#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DistanceSensor.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import gpiozero as gz

class DistanceSensor(gz.DistanceSensor):
    """超声波传感器"""

    def __init__(self, echo=None, trigger=None):
        super().__init__(echo=echo, trigger=trigger)

    def get_value(self):
        """返回测量的距离, 单位为厘米 (cm), 或使用 实例.distance 属性获取。"""
        return self.distance * 100
