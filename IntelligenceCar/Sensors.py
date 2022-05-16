#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Sensors.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from gpiozero import LineSensor
from gpiozero import DistanceSensor


class OCInfraredSensor():
    """红外避障传感器"""

    def __init__(self, *args, **kw) -> None:
        super.__init__(args, kw)

        pass


class OCDistanceSensor(DistanceSensor):
    """超声波传感器"""

    def __init__(self, *args, **kw) -> None:
        super.__init__(args, kw)

        pass


class OCLineSensor(LineSensor):
    """巡线传感器"""

    def __init__(self, *args, **kw) -> None:
        super.__init__(args, kw)

        pass


class LineSystem():
    """三个巡线传感器组成的巡线系统"""

    def __init__(self, left_pin, mid_pin, right_pin) -> None:
        self.line_left = OCLineSensor(left_pin)
        self.line_mid = OCLineSensor(mid_pin)
        self.line_right = OCLineSensor(right_pin)

    def state():
        """返回传感器状态"""
        pass
