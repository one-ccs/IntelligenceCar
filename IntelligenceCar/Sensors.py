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
    def __init__(self, *args, **kw):
        super.__init__(args, kw)

        pass


class OCDistanceSensor(DistanceSensor):
    """超声波传感器"""
    def __init__(self, *args, **kw):
        super.__init__(args, kw)

        pass


class OCLineSensor(LineSensor):
    """巡线传感器"""
    def __init__(self, *args, **kw):
        super.__init__(args, kw)

        pass
