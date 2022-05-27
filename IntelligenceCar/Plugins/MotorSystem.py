#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MotorSystem.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import RPi.GPIO as GPIO
from IntelligenceCar.Plugins.Logger import Logger

class MotorSystem(Logger):
    """
    四轮驱动器

    :参数 整型元组 pins:
        初始化电机 pin 接口的二维元组表 (
            (左前 pwm, 左前方向), (右前 pwm, 右前方向),
            (右后 pwm, 右后方向), (左后 pwm, 左后方向)
        )

    :属性 浮点型 speed:
        将电机的转速表示为 -100.0 (全速后退) 到 +100.0 (全速前进) 之间的浮点值。
    """

    def __init__(self, pins=(
        (None, None), None, (None, None), None
    )):
        self._speed = 35.0  # 轮子转动速度百分比
        self._left_direction = True
        self._right_direction = True

        self.left_pins = pins[0]
        self.left_pwm_pin = pins[1]
        self.right_pins = pins[2]
        self.right_pwm_pin = pins[3]
        self.left_pwm = None
        self.right_pwm = None

        self._setup_gpio()

    def _setup_gpio(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.left_pins[0], GPIO.OUT)
        GPIO.setup(self.left_pins[1], GPIO.OUT)
        GPIO.setup(self.left_pwm_pin, GPIO.OUT)
        self.left_pwm = GPIO.PWM(self.left_pwm_pin, 100)
        self.left_pwm.start(0)

        GPIO.setup(self.right_pins[0], GPIO.OUT)
        GPIO.setup(self.right_pins[1], GPIO.OUT)
        GPIO.setup(self.right_pwm_pin, GPIO.OUT)
        self.right_pwm = GPIO.PWM(self.right_pwm_pin, 100)
        self.right_pwm.start(0)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def left_direction(self):
        return self._left_direction

    @left_direction.setter
    def left_direction(self, direction=True):
        """设置左轮旋转方向"""
        if direction:
            # 正转
            GPIO.output(self.left_pins[0], True)
            GPIO.output(self.left_pins[1], False)
        else:
            GPIO.output(self.left_pins[0], False)
            GPIO.output(self.left_pins[1], True)
        self._left_direction = direction

    @property
    def right_direction(self):
        return self._right_direction

    @right_direction.setter
    def right_direction(self, direction=True):
        """设置右轮旋转方向"""
        if direction:
            # 正转
            GPIO.output(self.right_pins[0], True)
            GPIO.output(self.right_pins[1], False)
        else:
            GPIO.output(self.right_pins[0], False)
            GPIO.output(self.right_pins[1], True)
        self._right_direction = direction

    def stop(self):
        """停止"""
        self.log('<class MotorSystem> 停止')
        self.left_pwm.ChangeDutyCycle(0)
        self.right_pwm.ChangeDutyCycle(0)

    def forward(self):
        """前进"""
        self.log('<class MotorSystem> 前进')
        self.left_direction = True
        self.right_direction = True
        self.left_pwm.ChangeDutyCycle(self._speed)
        self.right_pwm.ChangeDutyCycle(self._speed)

    def backward(self):
        """后退"""
        self.log('<class MotorSystem> 后退')
        self.left_direction = False
        self.right_direction = False
        self.left_pwm.ChangeDutyCycle(self._speed)
        self.right_pwm.ChangeDutyCycle(self._speed)

    def turn_left(self):
        """左转"""
        self.log('<class MotorSystem> 左转')
        self.left_direction = False
        self.right_direction = True
        self.left_pwm.ChangeDutyCycle(self._speed)
        self.right_pwm.ChangeDutyCycle(self._speed)

    def turn_right(self):
        """右转"""
        self.log('右转')
        self.left_direction = True
        self.right_direction = False
        self.left_pwm.ChangeDutyCycle(self._speed)
        self.right_pwm.ChangeDutyCycle(self._speed)
