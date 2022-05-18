#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  launch.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Car import Car
from Server.Server import ic_server
from Demos import *


WHEELS_PIN = ((22, 18), (27, 18), (25, 23), (24, 23)) # 电机针脚
CAMERA_PIN = 0                                        # 摄像头针脚 暂未实现可忽略
INFRAREDS_PIN = (12, 16)                              # 红外避障传感器针脚
DISTANCE_PIN = (21, 20)                               # 超声波传感器针脚
LINES_PIN = (13, None, 26)                            # 寻线传感器针脚
BUZZER_PIN = 11                                       # 蜂鸣器针脚

# 定义智能小车
car = Car(
    wheels_pin=WHEELS_PIN,
    camera_pin=CAMERA_PIN,
    infrareds_pin=INFRAREDS_PIN,
    distance_pin=DISTANCE_PIN,
    lines_pin=LINES_PIN,
    buzzer_pin=BUZZER_PIN
)

# 启动服务器
ic_server.run()

# 开始演示
base_demo(car)
# sport_demo()
# line_demo()
# infrared_demo()
# distance_demo()
