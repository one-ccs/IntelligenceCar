#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  launch.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Car import Car

def main(args):
    car = Car(((0,1),(2,3),(4,5),(6,7)))
    
    help(car.wheels.left_front_wheel)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
