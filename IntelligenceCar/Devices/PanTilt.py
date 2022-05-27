#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Sensors.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from Servo import Servo

class PanTilt():
    """云台"""

    def __init__(self, vertical_pin=None, horizontal_pin=None):
        self.vertical = None
        self.horizontal = None

        if vertical_pin:
            self.vertical = Servo(vertical_pin)
        if horizontal_pin:
            self.horizontal = Servo(horizontal_pin)

    def move_up(self, deg):
        """向上转动指定度数。"""
        self.vertical.angle += deg

    def move_right(self, deg):
        """向右转动指定度数。"""
        self.horizontal.angle += deg

    def move_down(self, deg):
        """向下转动指定度数。"""
        self.vertical.angle -= deg

    def move_left(self, deg):
        """向左转动指定度数。"""
        self.horizontal.angle -= deg

    def orientation(self, coordinate={'x': None, 'y': None}):
        """以正前方为原点调整到指定位置。"""
        self.horizontal = coordinate['y']
        self.vertical = coordinate['x']
