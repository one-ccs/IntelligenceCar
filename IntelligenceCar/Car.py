#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Car.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
# import RPi.GPIO as GPIO
from time import sleep

from IntelligenceCar.Devices import InfraredSensor
from IntelligenceCar.Devices import DistanceSensor
from IntelligenceCar.Devices import LineSensor
from IntelligenceCar.Devices import TonalBuzzer
from IntelligenceCar.Devices import LEDBoard
from IntelligenceCar.Devices import Motor
from IntelligenceCar.Devices import Camera
from IntelligenceCar.Devices import PanTilt


class InfraredSystem():
    """两个红外避障传感器组成的避障系统"""

    def __init__(self, left_pin, right_pin) -> None:
        self.left = None
        self.right = None

        if left_pin:
            self.left = InfraredSensor(left_pin)
        if right_pin:
            self.right = InfraredSensor(right_pin)


class LineSystem():
    """三个巡线传感器组成的巡线系统"""

    def __init__(self, left_pin, mid_pin, right_pin) -> None:
        self.left = None
        self.mid = None
        self.right = None

        if left_pin:
            self.left = LineSensor(left_pin)
        if mid_pin:
            self.mid = LineSensor(mid_pin)
        if right_pin:
            self.right = LineSensor(right_pin)

    @property
    def state(self):
        """返回传感器状态"""
        return (self.left.value, self.mid.value, self.right)


class Lights():
    """led 车灯"""

    def __init__(self, left_pin, right_pin) -> None:
        self.lights = None

        if left_pin and right_pin:
            self.lights = LEDBoard(left_pin, right_pin, pwm=True)

    def set(self, left_brightness=1.0, right_brightness=1.0) -> None:
        """同时调节两个 led 的亮度, 取值为 0.0 熄灭到 1.0 高亮。"""
        self.lights.value = (left_brightness, right_brightness)

    def both_on(self) -> None:
        self.lights.on()

    def both_off(self) -> None:
        self.lights.off()


class MotorSystem():
    """
    四轮驱动器

    :参数 整型元组 pins:
        初始化电机 pin 接口的二维元组表 (
            (左前速度, 左前方向), (右前速度, 右前方向),
            (右后速度, 右后方向), (左后速度, 左后方向)
        )

    :属性 浮点型 speed:
        将电机的转速表示为 -100.0 (全速后退) 到 +100.0 (全速前进) 之间的浮点值。
    """

    def __init__(self, pins=((None, None), (None, None), (None, None), (None, None))) -> None:
        self._speed = 50.0 # 轮子转动速度百分比
        self.motors = [None, None, None, None] # 左前、右前、右后、左后电机

        for i in range(4):
            self.motors[i] = Motor(pins[i][0], pins[i][1])

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, speed: float) -> None:
        self._speed = speed

        for i in range(4):
            self.motors[i].speed = speed

    def stop(self) -> None:
        """停止"""
        for i in range(4):
            self.motors[i].stop()

    def forward(self) -> None:
        """前进"""
        for i in range(4):
            self.motors[i].forward()

    def backward(self) -> None:
        """后退"""
        for i in range(4):
            self.motors[i].backward()

    def turn_left(self) -> None:
        """左转"""
        self.motors[0].backward()
        self.motors[1].forward()
        self.motors[2].forward()
        self.motors[3].backward()

    def turn_right(self) -> None:
        """右转"""
        self.motors[0].forward()
        self.motors[1].backward()
        self.motors[2].backward()
        self.motors[3].forward()


class CameraSystem():
    """摄像系统"""

    def __init__(self) -> None:
        self.camera = Camera()
        self.pan_tilt = PanTilt()

    def track(self, image) -> None:
        """使摄像头瞄准目标物"""
        pass

    def autofocus(self) -> None:
        """自动对焦"""
        pass


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
        buzzer_pin=None,
        green_led_pin=None,
        red_led_pin=None
    ) -> None:
        self._STEER_TIME = 0.0    # 车子旋转 1° 需要的秒数
        self._STRAIGHT_TIME = 0.0  # 车子直行一单位 1cm 需要的秒数

        if wheels_pin:
            self.wheels = MotorSystem(wheels_pin)             # 车轮系统
        # if camera_pin:
        #     self.camera = CameraSystem(camera_pin)            # 摄像头
        if infrareds_pin:
            self.infrareds = InfraredSensor(infrareds_pin)  # 红外避障
        if distance_pin:
            self.distance = DistanceSensor(distance_pin)    # 超声波
        if lines_pin:
            self.lines = LineSystem(lines_pin)                # 巡线
        if buzzer_pin:
            self.buzzer = TonalBuzzer(buzzer_pin)           # 音调蜂鸣器

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
