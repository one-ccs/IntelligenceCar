#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Sensors.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from operator import le
from gpiozero import LineSensor
from gpiozero import DistanceSensor

from gpiozero import TonalBuzzer


class ICDistanceSensor(DistanceSensor):
    """超声波传感器"""

    def __init__(self, echo=None, trigger=None):
        super().__init__()

        pass


class ICLineSensor(LineSensor):
    """巡线传感器"""

    def __init__(self, pin=None):
        super().__init__(pin)

        pass


class LineSystem():
    """三个巡线传感器组成的巡线系统"""

    def __init__(self, left_pin, mid_pin, right_pin) -> None:
        self.left = None
        self.mid = None
        self.right = None

        if left_pin:
            self.left = ICLineSensor(left_pin)
        if mid_pin:
            self.mid = ICLineSensor(mid_pin)
        if right_pin:
            self.right = ICLineSensor(right_pin)

    @property
    def state(self):
        """返回传感器状态"""
        return (self.left.value, self.mid.value, self.right)


class ICInfraredSensor():
    """红外避障传感器"""

    def __init__(self, pin) -> None:

        pass


class InfraredSystem():
    """红外避障传感器系统"""

    def __init__(self, left_pin, right_pin) -> None:
        self.left = None
        self.right = None

        if left_pin:
            self.left = ICInfraredSensor(left_pin)
        if right_pin:
            self.right = ICInfraredSensor(right_pin)


class ICTonalBuzzer(TonalBuzzer):
    """音调蜂鸣器"""
    DO = 261.6
    RE = 293.6
    MI = 329.6
    FA = 349.2
    SO = 392.0
    LA = 440.0
    SI = 493.8

    def __init__(self, pin=None):
        super().__init__(pin)

        pass

    def play_song(self):
        """蜂鸣器演奏一首歌"""
        pass


class LED():
    """led 灯"""

    def __init__(self) -> None:
        pass
