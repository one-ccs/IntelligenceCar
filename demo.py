#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from math import sqrt

from IntelligenceCar.Car import Car
from IntelligenceCar.Devices import TonalBuzzer


def base_move_demo(car):
    """智能小车基础移动演示"""
    # 移动演示
    car.forward(10)
    car.backward(10)
    car.turn_left(360)
    car.turn_right(360)
    # led 演示

    # 超声波演示
    # 寻迹参数显示
    # 红外避障参数演示
    # 摄像头云台运动演示
    # 超声波伺服器运动演示


def sport_demo(car):
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


def buzzer_demo(car):
    # 蜂鸣器演示
    car.buzzer.play(TonalBuzzer.DO)
    car.buzzer.play(TonalBuzzer.RE)
    car.buzzer.play(TonalBuzzer.MI)
    car.buzzer.play(TonalBuzzer.FA)
    car.buzzer.play(TonalBuzzer.SO)
    car.buzzer.play(TonalBuzzer.LA)
    car.buzzer.play(TonalBuzzer.SI)


def line_demo(car):
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


def infrared_demo(car):
    """智能小车红外避障演示"""
    pass


def distance_demo(car):
    """智能小车超声波避障演示"""
    min_distance = 20

    while(True):
        if car.distance.value < min_distance:
            car.backward(4)
            car.turn_left(30)


def automatic_track_demo(car):
    """智能小车自动寻物演示"""
    pass


def main():
    WHEELS_PIN = ((22, 18), (27, 23), (25, 18), (24, 23))  # 电机针脚
    # CAMERA_PIN = 0                                         # 摄像头针脚 暂未实现可忽略
    # INFRAREDS_PIN = (12, 16)                               # 红外避障传感器针脚
    # DISTANCE_PIN = (21, 20)                                # 超声波传感器针脚
    # LINES_PIN = (13, None, 26)                             # 寻线传感器针脚
    # BUZZER_PIN = 11                                        # 蜂鸣器针脚
    # GREEN_LED = 5                                          # 绿色 led
    # RED_LED = 6                                            # 红色 led

    # 定义智能小车
    car = Car(
        wheels_pin=WHEELS_PIN,
        # camera_pin=CAMERA_PIN,
        # infrareds_pin=INFRAREDS_PIN,
        # distance_pin=DISTANCE_PIN,
        # lines_pin=LINES_PIN,
        # buzzer_pin=BUZZER_PIN
    )
    base_move_demo(car)

    return


if __name__ == '__main__':
    main()
