#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Motor.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import RPi.GPIO as GPIO

from IntelligenceCar.Plugins.Logger import Logger


class Motor(Logger):
    """电机

    :参数 整型 p_pin:
        转速控制针脚 (pwm 针脚)。

    :参数 整型 f_pin:
        旋转方向控制引脚。
    """
    left_pwm_pin = None
    left_pwm = None
    right_pwm_pin = None
    right_pwm = None

    def __init__(self, p_pin, f_pin, id=None):
        self.log('正在初始化, p_pin: {}, f_pin: {}, id: {}'.format(
            p_pin, f_pin, id))
        self._speed = 30.0       # 转速占空比
        self._frequency = 100.0  # pwm 频率 (Hz)
        self._id = id

        self.p_pin = p_pin
        self.f_pin = f_pin
        self.pwm = None

        if p_pin and f_pin:
            GPIO.setwarnings(False)     # 关闭警告信息
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(p_pin, GPIO.OUT)
            GPIO.setup(f_pin, GPIO.OUT)
            if p_pin != Motor.left_pwm_pin and p_pin != Motor.right_pwm_pin and Motor.left_pwm == None:
                Motor.left_pwm_pin = p_pin
                self.pwm = GPIO.PWM(p_pin, self._frequency)
                self.pwm.start(0)
            if p_pin != Motor.left_pwm_pin and p_pin != Motor.right_pwm_pin and Motor.right_pwm == None:
                Motor.right_pwm_pin = p_pin
                self.pwm = GPIO.PWM(p_pin, self._frequency)
                self.pwm.start(0)
        else:
            raise ValueError('初始化 class Motor 的参数 p_pin 或 f_pin 为无效值。')

    def __del__(self):
        self.pwm.stop()

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        """通过控制 pwm 占空比调节电机转速"""
        if speed < -100.0 or speed > 100.0:
            raise ValueError("无效的参数 speed, 应为 -100.0 到 +100.0 之间的数字。")
        else:
            self._speed = speed
            self.log('(' + str(self._id) +
                     ') 设置速度 ' + str(self._speed))

    @property
    def frequency(self):
        """pwm 频率"""
        return self._frequency

    @frequency.setter
    def frequency(self, hz):
        self._frequency = hz
        self.pwm = GPIO.PWM(self.p_pin, hz)

    def forward(self):
        """前进"""
        self.pwm.ChangeDutyCycle(abs(self._speed))
        GPIO.output(self.f_pin, True)
        self.log('(' + str(self._id) +
                 ') 正转, 速度 ' + str(self._speed))

    def backward(self):
        """后退"""
        self.pwm.ChangeDutyCycle(abs(self._speed))
        GPIO.output(self.f_pin, False)
        self.log('(' + str(self._id) +
                 ') 反转, 速度 ' + str(self._speed))

    def stop(self):
        """停止"""
        self.pwm.ChangeDutyCycle(0)
        self.log('(' + str(self._id) + ') 停止')
