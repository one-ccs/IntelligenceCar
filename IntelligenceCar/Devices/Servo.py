#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Servo.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import gpiozero as gz

class Servo(gz.AngularServo):
    """舵机"""

    def __init__(self, pin=None, initial_angle=0, min_angle=-90, max_angle=90):
        super().__init__(pin, initial_angle, min_angle, max_angle)
