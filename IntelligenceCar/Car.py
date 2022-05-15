#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Car.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
# import RPi.GPIO as GPIO
from time import sleep
from turtle import forward

from IntelligenceCar.Wheel import WheelSystem
from IntelligenceCar.Camera import CameraSystem
from IntelligenceCar.Sensors import InfraredSensor
from IntelligenceCar.Sensors import UltrasonicSensor
from IntelligenceCar.Sensors import TrackingSensor


class Car():
    """智能小车"""
    def __init__(self):
        self._STEER_TIME = 0.36    # 车子旋转一度需要的秒数
        self._STRAIGHT_TIME = 0.36 # 车子直行一单位 () 需要的秒数
        
        self.wheels = WheelSystem()          # 车轮系统
        self.camera = CameraSystem()         # 摄像头
        self.infrared = InfraredSensor()     # 红外避障
        self.ultrasonic = UltrasonicSensor() # 超声波
        self.track = TrackingSensor()        # 寻迹

    def turn_left(self, deg):
        """
        向左旋转指定度数。
        """
        self.wheels.turn_left()
        sleep(self._STEER_TIME * deg)
        self.wheels.stop()

    def turn_right(self, deg):
        """
        向右旋转指定度数。
        """
        self.wheels.turn_right()
        sleep(self._STEER_TIME * deg)
        self.wheels.stop()

    def forward(self, distance):
        """
        向前指定单位的距离。
        """
        self.wheels.forward()
        sleep(self._STRAIGHT_TIME * distance)
        self.wheels.stop()
        self.wheels.stop()

    def backward(self, distance):
        """
        向前指定单位的距离。
        """
        self.wheels.backward()
        sleep(self._STRAIGHT_TIME * distance)
        self.wheels.stop()

    def track_demo(self):
        """寻迹演示"""
        pass

    def infrared_demo(self):
        """红外避障演示"""
        pass

    def automatic_track_demo(self):
        """自动寻物演示"""
        pass
