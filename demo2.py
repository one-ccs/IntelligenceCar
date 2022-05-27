#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from time import sleep
from IntelligenceCar.Functions import *


def test1():
    """单轮测试"""
    run1()
    run1_1() # 左前进

    run2()
    run2_2() # 左后退

    run3()
    run3_3() # 右后退

    run4()
    run4_4() # 右前进

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


def test5():
    setup_infrareds()
    start_infrared()
    clean_infrareds()


def test6():
    setup_distance()
    start_distance()
    clean_distance()


def test7():
    setup_lines()
    start_line()
    clean_lines()


def test8():
    setup_buzzer()
    play_song()
    clean_buzzer()


def test8():
    green = False
    red = True

    for i in range(10):
        set_green_led(not green)
        set_red_led(not red)

        green = not green
        red = not red


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
