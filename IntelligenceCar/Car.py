#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Car.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
# import RPi.GPIO as GPIO
from time import sleep

from IntelligenceCar.Wheel import WheelSystem
from IntelligenceCar.Camera import CameraSystem
from IntelligenceCar.Sensors import OCInfraredSensor
from IntelligenceCar.Sensors import OCDistanceSensor
from IntelligenceCar.Sensors import OCLineSensor


class Car():
    """智能小车"""
    def __init__(
        self,
        wheels_pin=((),(),(),()),
        camera_pin=None,
        infrared_pin=None,
        distance_pin=None,
        line_pin=None
    ):
        self._STEER_TIME = 0.36    # 车子旋转一度需要的秒数
        self._STRAIGHT_TIME = 0.36 # 车子直行一单位 (厘米) 需要的秒数

        self.wheels = WheelSystem(wheels_pin)          # 车轮系统
        self.camera = CameraSystem(camera_pin)         # 摄像头
        self.infrared = OCInfraredSensor(infrared_pin) # 红外避障
        self.distance = OCDistanceSensor(distance_pin) # 超声波
        self.line = OCLineSensor(line_pin)             # 巡线

    def turn_left(self, deg:int):
        """
        向左旋转指定度数。
        """
        self.wheels.turn_left()
        sleep(self._STEER_TIME * deg)
        self.wheels.stop()

    def turn_right(self, deg:int):
        """
        向右旋转指定度数。
        """
        self.wheels.turn_right()
        sleep(self._STEER_TIME * deg)
        self.wheels.stop()

    def forward(self, distance:int):
        """
        向前指定单位的距离。
        """
        self.wheels.forward()
        sleep(self._STRAIGHT_TIME * distance)
        self.wheels.stop()
        self.wheels.stop()

    def backward(self, distance:int):
        """
        向前指定单位的距离。
        """
        self.wheels.backward()
        sleep(self._STRAIGHT_TIME * distance)
        self.wheels.stop()

    def line_demo(self):
        """巡线演示"""
        pass

    def infrared_demo(self):
        """红外避障演示"""
        pass

    def automatic_track_demo(self):
        """自动寻物演示"""
        pass
