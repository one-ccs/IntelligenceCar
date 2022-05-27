#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Car.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from time import sleep

from Devices.InfraredSensor import InfraredSensor
from Devices.DistanceSensor import DistanceSensor
from Devices.LEDBoard import LEDBoard
from Devices.TonalBuzzer import TonalBuzzer
from Plugins.Logger import Logger
from Plugins.MotorSystem import MotorSystem
from Plugins.LineSystem import LineSystem


# 电机针脚常量
LEFT_FRONT_PIN = 22  # AIN1
LEFT_REAR_PIN = 27   # AIN2
LEFT_PWM_PIN = 18    # PWMA
RIGHT_FRONT_PIN = 25  # BIN1
RIGHT_REAR_PIN = 24  # BIN2
RIGHT_PWM_PIN = 23   # PWMB
# 红外避障传感器针脚
INFRAREDS_LEFT_PIN = 12
INFRAREDS_RIGHT_PIN = 16
# 超声波传感器针脚
DISTANCE_ECHO_PIN = 21
DISTANCE_TRIGGER_PIN = 20
# 寻线传感器针脚
LINES_LEFT_PIN = 13
LINES_MID_PIN = None
LINES_RIGHT_PIN = 26
# 蜂鸣器针脚常量
BUZZER_PIN = 11
# LED 针脚
GREEN_LED = 5
RED_LED = 6


class Car(Logger):
    """智能小车

    :参数 整型元组 wheels_pin:
        四个电机的针脚 (
            (左电机 1, 左电机 2), 左 pwm,
            (右电机 1, 右电机 2), 右 pwm
        )。

    :参数 整型元组 infrareds_pin:
        红外避障传感器针脚 (左, 右)。

    :参数 整型元组 distance_pin:
        超声波 (距离) 传感器针脚 (echo, trigger)。

    :参数 整型元组 lines_pin:
        寻线传感器针脚 (左, 中, 右)。

    :参数 整型 buzzer_pin:
        蜂鸣器针脚。
    """
    STEER_TIME = 0.002     # 车子旋转 1° 需要的秒数
    STRAIGHT_TIME = 0.2  # 车子直行一单位 1cm 需要的秒数

    def __init__(
        self,
        wheels_pin=((None, None), None, (None, None), None),
        infrareds_pin=(None, None),
        distance_pin=(None, None),
        lines_pin=(None, None, None),
        leds_pin=(None, None),
        buzzer_pin=None
    ):
        self._green_light = False
        self._red_light = False

        self.wheels = None
        self.infrareds = None
        self.distance = None
        self.lines = None
        self.lights = None
        self.buzzer = None

        if wheels_pin:
            self.wheels = MotorSystem(wheels_pin)             # 车轮系统
        if infrareds_pin:
            self.infrareds = InfraredSensor(infrareds_pin)    # 红外避障
        if distance_pin:
            self.distance = DistanceSensor(distance_pin)      # 超声波
        if lines_pin:
            self.lines = LineSystem(lines_pin)                # 巡线
        if leds_pin:
            self.lights = LEDBoard(leds_pin[0], leds_pin[1])  # LED
        if buzzer_pin:
            self.buzzer = TonalBuzzer(buzzer_pin)             # 音调蜂鸣器

    def stop(self):
        """停止"""
        self.log('<class Car> 停止')
        self.wheels.stop()

    def forward(self, distance):
        """
        向前指定单位 1cm 的距离。

        :参数 整型 deg:
            要选择的度数。
        """
        self.log('<class Car> 前进 {} 单位, {} 秒'.format(
            distance, Car.STRAIGHT_TIME * distance))
        self.wheels.forward()
        sleep(Car.STRAIGHT_TIME * distance)
        self.wheels.stop()

    def backward(self, distance):
        """
        向前指定单位 1cm 的距离。

        :参数 整型 deg:
            要选择的度数。
        """
        self.log('<class Car> 后退 {} 单位, {} 秒'.format(
            distance, Car.STRAIGHT_TIME * distance))
        self.wheels.backward()
        sleep(Car.STRAIGHT_TIME * distance)
        self.wheels.stop()

    def turn_left(self, deg):
        """
        向左旋转指定度数。

        :参数 整型 deg:
            要选择的度数。
        """
        self.log('<class Car> 向左旋转 {} 单位, {} 秒'.format(
            deg, Car.STRAIGHT_TIME * deg))
        self.wheels.turn_left()
        sleep(Car.STEER_TIME * deg)
        self.wheels.stop()

    def turn_right(self, deg):
        """
        向右旋转指定度数。

        :参数 整型 deg:
            要选择的度数。
        """
        self.log('<class Car> 向右旋转 {} 单位, {} 秒'.format(
            deg, Car.STRAIGHT_TIME * deg))
        self.wheels.turn_right()
        sleep(Car.STEER_TIME * deg)
        self.wheels.stop()

    def get_distance(self):
        """获取超声波传感器数值, 单位 cm."""
        return self.distance.get_value()

    def turn_both_light_on(self):
        pass

    def turn_both_light_off(self):
        pass

    def turn_light_alternate(self):
        """交替闪烁"""
        pass
