#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from IntelligenceCar.Car import *


# 定义智能小车
car = Car(
    wheels_pin=(
        (LEFT_FRONT_PIN, LEFT_REAR_PIN), LEFT_PWM_PIN,
        (RIGHT_FRONT_PIN, RIGHT_REAR_PIN), RIGHT_PWM_PIN
    ),
    infrareds_pin=(
        INFRAREDS_LEFT_PIN,
        INFRAREDS_RIGHT_PIN
    ),
    distance_pin=(
        DISTANCE_ECHO_PIN,
        DISTANCE_TRIGGER_PIN
    ),
    lines_pin=(
        LINES_LEFT_PIN,
        LINES_MID_PIN,
        LINES_RIGHT_PIN
    ),
    leds_pin=(
        GREEN_LED_PIN,
        RED_LED_PIN
    ),
    buzzer_pin=BUZZER_PIN,
    distance_servo_pin=DISTANCE_SERVO_PIN,
    camera_servos_pin=(
        CAMERA_HORIZONTAL_SERVO_PIN,
        CAMERA_VERTICAL_SERVO_PIN
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

    # test2()

    # test3()

    # test4()


    car.start_line()
    # car.start_infrared()
    # car.start_distance()
    # car.start_dis_inf()

    return


if __name__ == '__main__':
    main()