#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Car.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
# import RPi.GPIO as GPIO
from Wheel import WheelSystem
from Camera import CameraSystem
from Sensors import InfraredSensor
from Sensors import UltrasonicSensor
from Sensors import TrackingSensor


class Car():
    """智能小车"""
    def __init__(self):
        self.wheels = WheelSystem()          # 车轮系统
        self.camera = CameraSystem()         # 摄像头
        self.infrared = InfraredSensor()     # 红外避障
        self.ultrasonic = UltrasonicSensor() # 超声波
        self.track = TrackingSensor()        # 寻迹

    def track_demo(self):
        """寻迹演示"""
        pass

    def infrared_demo(self):
        """红外避障演示"""
        pass

    def automatic_track_demo(self):
        """自动寻物演示"""
        pass


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
