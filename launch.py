#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  launch.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from math import sqrt

from IntelligenceCar.Car import Car

# 针脚定义
# 电机针脚:  ((左前速度, 左前方向), (右前速度, 右前方向), (右后速度, 右后方向), (左后速度, 左后方向))
WHEELS_PIN = ((22, 18), (27, 18), (25, 23), (24, 23))
# 摄像头针脚 暂未实现可忽略
CAMERA_PIN = 0
# 红外避障传感器针脚 (左, 右)
INFRAREDS_PIN = (12, 16)
# 超声波传感器针脚 (回声针脚 echo, 触发针脚 trigger)
DISTANCE_PIN = (21, 20)
# 寻线传感器针脚 (左, 中, 右)
LINES_PIN = (13, None, 26)
# 蜂鸣器针脚
BUZZER_PIN = 11

# 定义智能小车
car = Car(WHEELS_PIN, CAMERA_PIN, INFRAREDS_PIN,
          DISTANCE_PIN, LINES_PIN, BUZZER_PIN)


def move_demo() -> None:
    """前进后退转向演示"""
    car.forward(10)
    car.backward(10)
    car.turn_left(360)
    car.turn_right(360)


def sport_demo() -> None:
    """智能小车运动演示"""
    # 走一个正方形
    for i in range(4):
        # 前进 100 cm
        car.forward(100)
        # 右转 90°
        car.turn_right(90)

    # 走一个 "又" 字
    car.turn_right(45)
    car.forward(100 * sqrt(2))
    car.turn_right(45)
    car.backward(100)
    car.turn_right(45)
    car.forward(100)

    # 回到起点
    car.turn_left(225)
    car.forward(100)
    car.turn_left(270)


def line_demo(self) -> None:
    """智能小车巡线演示"""
    for i in range(500):
        if car.lines.state == (False, True, False):
            # 在中心线 直行
            car.forward(4)
        elif car.lines.state == (True, False, False):
            # 偏右 向左转
            car.turn_left(15)
        elif car.lines.state == (False, False, True):
            # 偏左 向右转
            car.turn_right(15)


def infrared_demo(self) -> None:
    """智能小车红外避障演示"""
    pass


def distance_demo() -> None:
    """智能小车超声波避障演示"""
    min_distance = 20

    while(True):
        if car.distance.value < min_distance:
            car.backward(4)
            car.turn_left(30)


def automatic_track_demo(self) -> None:
    """智能小车自动寻物演示"""
    pass


def main(args):
    move_demo()
    # sport_demo()
    # line_demo()
    # infrared_demo()
    # distance_demo()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
