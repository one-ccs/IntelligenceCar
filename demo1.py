#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from IntelligenceCar.Car import Car

# 电机针脚 ((左前 pwm, 左前方向), (右前 pwm, 右前方向), (右后 pwm, 右后方向), (左后 pwm, 左后方向))
WHEELS_PIN = ((18, 22), (23, 25), (23, 24), (18, 27))

car = Car(WHEELS_PIN)


def test1():
    """单轮测试"""
    pass


def test2():
    """移动测试"""
    car.forward(10)


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
