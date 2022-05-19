#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from time import sleep
from IntelligenceCar.Functions import *


def test1():
    """单轮测试"""
    run1()
    sleep(2)
    run1_1()
    sleep(2)

    run2()
    sleep(2)
    run2_2()
    sleep(2)

    run3()
    sleep(2)
    run3_3()
    sleep(2)

    run4()
    sleep(2)
    run4_4()
    sleep(2)

    stop()


def test2():
    """移动测试"""
    forward()
    backward()
    turn_left()
    turn_right()

    stop()


def test3():
    """速度 15 向左旋转 10s"""
    turn_left(15, 10)
    stop()


def test4():
    """速度 15 直行 10s"""
    forward(15, 10)


def main():
    test1()

    # test2()

    # test3()

    # test4()

    return


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()