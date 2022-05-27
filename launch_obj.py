#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  launch_obj.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Car import *
from Server.Server_obj import run


if __name__ == '__main__':
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

    # 启动服务器
    # run(car)
    car.set_servo()
