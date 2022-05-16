#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Camera.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
class Camera():
    """摄像头"""
    def __init__(self):
        pass

    def shoot(self):
        """拍摄一张照片"""
        pass

    def upload(self):
        """上传照片"""
        pass

    def video(self):
        """实时录像"""
        pass


class PanTilt():
    """摄像头云台"""
    def __init__(self):
        pass

    def move_up(self, distance):
        """向上"""
        pass

    def move_right(self, distance):
        """向右"""
        pass

    def move_down(self, distance):
        """向下"""
        pass

    def move_left(self, distance):
        """向左"""
        pass

    def orientation(self, coordinate):
        """定位到指定位置"""
        pass


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
