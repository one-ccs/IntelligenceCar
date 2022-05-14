#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  launch.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from IntelligenceCar.Car import Car

def main(args):
    car = Car()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
