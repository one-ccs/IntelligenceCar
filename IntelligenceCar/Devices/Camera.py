#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Camera.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import cv2

class Camera():
    """摄像头"""

    def __init__(self, width=480, height=270):
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def __del__(self):
        self.camera.release()
        cv2.destroyAllWindows()

    def shoot(self):
        """拍摄一张照片"""
        _, frame = self.camera.read()
        return frame

    def upload(self):
        """上传照片"""
        pass

    def video(self):
        """实时录像"""
        pass
