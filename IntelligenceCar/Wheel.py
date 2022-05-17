#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Wheel.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import RPI.GPIO as GPIO


class Motor():
    """电机

    :参数 整型 p_pin:
        转速控制针脚 (pwm 针脚)。

    :参数 整型 f_pin:
        旋转方向控制引脚。
    """

    def __init__(self, p_pin, f_pin):
        self._speed = 50.0      # 转速占空比
        self._frequency = 100.0  # pwm 频率 (Hz)

        self.p_pin = p_pin
        self.f_pin = f_pin

        GPIO.setwarnings(False)     # 关闭警告信息
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(p_pin, GPIO.OUT)
        GPIO.setup(f_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(p_pin, self._frequency)
        self.pwm.start(0)

    def __del__(self):
        self.pwm.stop()

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, speed: float) -> None:
        """通过控制 pwm 占空比调节电机转速"""
        if speed < -100.0 or speed > 100.0:
            raise ValueError("无效的参数 speed, 应为 -100.0 到 +100.0 之间的数字。")

    @property
    def frequency(self) -> float:
        """pwm 频率"""
        return self._frequency

    @frequency.setter
    def frequency(self, hz: float) -> None:
        self._frequency = hz
        self.pwm = GPIO.PWM(self.p_pin, hz)

    def forward(self) -> None:
        """前进"""
        self.pwm.ChangeDutyCycle(abs(self._speed))
        GPIO.output(self.f_pin, True)

    def backward(self) -> None:
        """后退"""
        self.pwm.ChangeDutyCycle(abs(self._speed))
        GPIO.output(self.f_pin, False)

    def stop(self) -> None:
        """停止"""
        self.pwm.ChangeDutyCycle(0)


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
