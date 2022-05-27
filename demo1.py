#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from IntelligenceCar.Car import *

car = Car(
    (
        (LEFT_FRONT_PIN, LEFT_REAR_PIN), LEFT_PWM_PIN,
        (RIGHT_FRONT_PIN, RIGHT_REAR_PIN), RIGHT_PWM_PIN
    )
)


def test1():
    """单轮测试"""
    pass


def test2():
    """移动测试"""
    car.forward(10)
    car.backward(10)
    car.turn_left(360)
    car.turn_right(360)


def test3():
    """速度 15 向左旋转 10s"""


def test4():
    """速度 15 直行 10s"""


def main():
    # test1()

    test2()

    # test3()

    # test4()

    return


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
