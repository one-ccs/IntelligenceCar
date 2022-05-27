#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CameraSystem.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Devices.Camera import Camera
from IntelligenceCar.Devices.PanTilt import PanTilt

class CameraSystem():
    """摄像系统"""

    def __init__(self):
        self.camera = Camera()
        self.pan_tilt = PanTilt()

    def track(self, image):
        """使摄像头瞄准目标物"""
        pass

    def autofocus(self):
        """自动对焦"""
        pass
