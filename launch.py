#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  launch.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Car import Car

# 针脚定义
WHEELS_PIN = ((0,0),(0,0),(0,0),(0,0))
CAMERA_PIN = 0
INFRARED_PIN = 0
DISTANCE_PIN = 0
LINE_PIN = 0


def main(args):
    car = Car(WHEELS_PIN, CAMERA_PIN, INFRARED_PIN, DISTANCE_PIN, LINE_PIN)
    
    help(car.wheels.left_front_wheel)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
