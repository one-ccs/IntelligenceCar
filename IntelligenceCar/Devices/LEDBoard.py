#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  LEDBoard.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import gpiozero as gz

class LEDBoard(gz.LEDBoard):
    """课同时空时控制多个 led"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pass
