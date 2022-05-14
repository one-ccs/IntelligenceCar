#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Wheel.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from gpiozero import Motor


# class Motor(Motor):
#     """车轮"""
#     def __init__(self, speed):
#         self.enabled


class WheelSystem():
    """四轮驱动器"""
    def __init__(self, speed=5):
        self._speed = speed

        self.left_front_wheel = Motor(self._speed)  # 左前轮
        self.right_front_wheel = Motor(self._speed) # 右前轮
        self.right_rear_wheel = Motor(self._speed)  # 右后轮
        self.left_rear_wheel = Motor(self._speed)   # 左后轮

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, int):
            return
        self._speed = speed

    def stop(self):
        """停止"""
        self.left_front_wheel.stop()
        self.right_front_wheel.stop()
        self.right_rear_wheel.stop()
        self.left_rear_wheel.stop()

    def forward(self):
        """前进"""
        self.left_front_wheel.forward()
        self.right_front_wheel.forward()
        self.right_rear_wheel.forward()
        self.left_rear_wheel.forward()

    def backward(self):
        """后退"""
        self.left_front_wheel.backward()
        self.right_front_wheel.backward()
        self.right_rear_wheel.backward()
        self.left_rear_wheel.backward()

    def turn_left(self):
        """左转"""
        self.left_front_wheel.backward()
        self.right_front_wheel.forward()
        self.right_rear_wheel.forward()
        self.left_rear_wheel.backward()

    def turn_right(self):
        """右转"""
        self.left_front_wheel.forward()
        self.right_front_wheel.backward()
        self.right_rear_wheel.backward()
        self.left_rear_wheel.forward()


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
