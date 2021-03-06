#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from time import sleep
from IntelligenceCar.Functions import *


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
    test2()

    # test3()

    # test4()

    return


if __name__ == '__main__':
    main()
