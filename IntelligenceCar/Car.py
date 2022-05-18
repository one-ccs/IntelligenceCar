#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Car.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
# import RPi.GPIO as GPIO
from dis import dis
from time import sleep

from IntelligenceCar.Wheel import MotorSystem
# from IntelligenceCar.Camera import CameraSystem
from IntelligenceCar.Devices import ICInfraredSensor
from IntelligenceCar.Devices import ICDistanceSensor
from IntelligenceCar.Devices import ICLineSensor
from IntelligenceCar.Devices import ICTonalBuzzer
from IntelligenceCar.Devices import LED


class InfraredSystem():
    """两个红外避障传感器组成的避障系统"""

    def __init__(self, left_pin, right_pin) -> None:
        self.left = None
        self.right = None

        if left_pin:
            self.left = ICInfraredSensor(left_pin)
        if right_pin:
            self.right = ICInfraredSensor(right_pin)


class LineSystem():
    """三个巡线传感器组成的巡线系统"""

    def __init__(self, left_pin, mid_pin, right_pin) -> None:
        self.left = None
        self.mid = None
        self.right = None

        if left_pin:
            self.left = ICLineSensor(left_pin)
        if mid_pin:
            self.mid = ICLineSensor(mid_pin)
        if right_pin:
            self.right = ICLineSensor(right_pin)

    @property
    def state(self):
        """返回传感器状态"""
        return (self.left.value, self.mid.value, self.right)


class Lights():
    """led 车灯"""

    def __init__(self, left_pin, right_pin) -> None:
        self.left = None
        self.right = None

        if left_pin:
            self.left = LED(left_pin)
        if right_pin:
            self.right = LED(right_pin)


class Car():
    """智能小车

    :参数 整型二维元组 wheels_pin:
        四个电机的针脚 (
            (左前速度, 左前方向), (右前速度, 右前方向),
            (右后速度, 右后方向), (左后速度, 左后方向)
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

        if wheels_pin:
            self.wheels = MotorSystem(wheels_pin)             # 车轮系统
        # if camera_pin:
        #     self.camera = CameraSystem(camera_pin)            # 摄像头
        if infrareds_pin:
            self.infrareds = ICInfraredSensor(infrareds_pin)  # 红外避障
        if distance_pin:
            self.distance = ICDistanceSensor(distance_pin)    # 超声波
        if lines_pin:
            self.lines = LineSystem(lines_pin)                # 巡线
        if buzzer_pin:
            self.buzzer = ICTonalBuzzer(buzzer_pin)           # 音调蜂鸣器

    def stop(self):
        """停止"""
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
