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
from IntelligenceCar.Devices import ICInfraredSensor
from IntelligenceCar.Devices import ICDistanceSensor
from IntelligenceCar.Devices import LineSystem
from IntelligenceCar.Devices import ICTonalBuzzer


class Car():
    """智能小车
    
    :参数 整型二维元组 wheels_pin:
        四个电机的针脚 (
            (左前前进, 左前后退), (右前前进, 右前后退),
            (右后前进, 右后后退), (左后前进, 左后后退)
        )。

    :参数 整型 camera_pin:
        摄像头针脚。

    :参数 整型元组 infrareds_pin:
        红外避障传感器针脚 (左, 右)。

    :参数 整型元组 distance_pin:
        超声波 (距离) 传感器针脚 (echo, trigger)。

    :参数 整型元组 lines_pin:
        寻线传感器针脚 (左, 中, 右)。

    :参数 整型 buzzer_pin:
        蜂鸣器针脚。
    """

    def __init__(
        self,
        wheels_pin=((None, None), (None, None), (None, None), (None, None)),
        camera_pin=None,
        infrareds_pin=(None, None),
        distance_pin=(None, None),
        lines_pin=(None, None, None),
        buzzer_pin=None
    ) -> None:
        self._STEER_TIME = 0.0    # 车子旋转 1° 需要的秒数
        self._STRAIGHT_TIME = 0.0  # 车子直行一单位 1cm 需要的秒数

        self.wheels = WheelSystem(wheels_pin)             # 车轮系统
        self.camera = CameraSystem(camera_pin)            # 摄像头
        self.infrareds = ICInfraredSensor(infrareds_pin)  # 红外避障
        self.distance = ICDistanceSensor(distance_pin)    # 超声波
        self.lines = LineSystem(lines_pin)                # 巡线
        self.buzzer = ICTonalBuzzer(buzzer_pin)           # 音调蜂鸣器

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

    def backward(self, distance: int) -> None:
        """
        向前指定单位 1cm 的距离。

        :参数 整型 deg:
            要选择的度数。
        """
        self.wheels.backward()
        sleep(self._STRAIGHT_TIME * distance)
        self.wheels.stop()
