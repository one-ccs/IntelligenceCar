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
from IntelligenceCar.Devices import OCInfraredSensor
from IntelligenceCar.Devices import OCDistanceSensor
from IntelligenceCar.Devices import LineSystem


class Car():
    """智能小车"""

    def __init__(
        self,
        wheels_pin=((None, None), (None, None), (None, None), (None, None)),
        camera_pin=None,
        infrareds_pin=(None, None),
        distance_pin=None,
        lines_pin=(None, None)
    ) -> None:
        self._STEER_TIME = 0.0    # 车子旋转 1° 需要的秒数
        self._STRAIGHT_TIME = 0.0  # 车子直行一单位 1cm 需要的秒数

        self.wheels = WheelSystem(wheels_pin)           # 车轮系统
        # self.camera = CameraSystem(camera_pin)          # 摄像头
        self.infrared = OCInfraredSensor(infrareds_pin)  # 红外避障
        self.distance = OCDistanceSensor(distance_pin)  # 超声波
        self.line = LineSystem(lines_pin)               # 巡线z

    def turn_left(self, deg: int) -> None:
        """
        向左旋转指定度数。

        :参数 整型 deg:
            要选择的度数。
        """
        self.wheels.turn_left()
        sleep(self._STEER_TIME * deg)
        self.wheels.stop()

    def turn_right(self, deg: int) -> None:
        """
        向右旋转指定度数。

        :参数 整型 deg:
            要选择的度数。
        """
        self.wheels.turn_right()
        sleep(self._STEER_TIME * deg)
        self.wheels.stop()

    def forward(self, distance: int) -> None:
        """
        向前指定单位 1cm 的距离。

        :参数 整型 deg:
            要选择的度数。
        """
        self.wheels.forward()
        sleep(self._STRAIGHT_TIME * distance)
        self.wheels.stop()
        self.wheels.stop()

    def backward(self, distance: int) -> None:
        """
        向前指定单位 1cm 的距离。

        :参数 整型 deg:
            要选择的度数。
        """
        self.wheels.backward()
        sleep(self._STRAIGHT_TIME * distance)
        self.wheels.stop()
