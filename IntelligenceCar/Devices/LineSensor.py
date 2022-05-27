#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  LineSensor.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import gpiozero as gz

class LineSensor(gz.LineSensor):
    """巡线传感器"""

    def __init__(self, pin=None):
        super().__init__(pin)

    def get_value(self):
        """返回值接近 0 表示检测到黑色, 接近 1 表示接近白色。"""
        return self.value
