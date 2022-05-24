#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  launch.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Car import Car
from Server.Server import ic_server


# 电机针脚常量
LEFT_FRONT_PIN = 22  # AIN1
LEFT_REAR_PIN = 27   # AIN2
LEFT_PWM_PIN = 18    # PWMA
RIGHT_FRONT_PIN = 25  # BIN1
RIGHT_REAR_PIN = 24  # BIN2
RIGHT_PWM_PIN = 23   # PWMB
# 红外避障传感器针脚
INFRAREDS_LEFT_PIN = 12
INFRAREDS_RIGHT_PIN = 16
# 超声波传感器针脚
DISTANCE_ECHO_PIN = 21
DISTANCE_TRIGGER_PIN = 21
# 寻线传感器针脚
LINES_LEFT_PIN = 13
LINES_MID_PIN = None
LINES_RIGHT_PIN = 26
# 蜂鸣器针脚常量
BUZZER_PIN = 11
# LED 针脚
GREEN_LED = 5
RED_LED = 6


# 定义智能小车
car = Car(
    wheels_pin=(
        (LEFT_PWM_PIN, LEFT_FRONT_PIN),
        (RIGHT_PWM_PIN, RIGHT_FRONT_PIN),
        (RIGHT_PWM_PIN, RIGHT_REAR_PIN),
        (LEFT_PWM_PIN, LEFT_REAR_PIN)
    ),
    # infrareds_pin=(
    #     INFRAREDS_LEFT_PIN,
    #     INFRAREDS_RIGHT_PIN
    # ),
    # distance_pin=(
    #     DISTANCE_ECHO_PIN,
    #     DISTANCE_TRIGGER_PIN
    # ),
    # lines_pin=(
    #     LINES_LEFT_PIN,
    #     LINES_MID_PIN,
    #     LINES_RIGHT_PIN
    # ),
    # buzzer_pin=BUZZER_PIN
)

# 启动服务器
# ic_server.run()
