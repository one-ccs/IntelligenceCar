#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Sensors.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from gpiozero import LineSensor
from gpiozero import DistanceSensor

from gpiozero import TonalBuzzer


class ICDistanceSensor(DistanceSensor):
    """超声波传感器"""

    def __init__(self, echo=None, trigger=None, queue_len=9, max_distance=1, threshold_distance=0.3, partial=False, pin_factory=None):
        super().__init__(echo, trigger, queue_len, max_distance,
                         threshold_distance, partial, pin_factory)

        pass


class ICLineSensor(LineSensor):
    """巡线传感器"""

    def __init__(self, pin=None, pull_up=False, active_state=None, queue_len=5, sample_rate=100, threshold=0.5, partial=False, pin_factory=None):
        super().__init__(pin, pull_up, active_state, queue_len,
                         sample_rate, threshold, partial, pin_factory)

        pass


class LineSystem():
    """三个巡线传感器组成的巡线系统"""

    def __init__(self, left_pin, mid_pin, right_pin) -> None:
        self.line_left = ICLineSensor(left_pin)
        self.line_mid = ICLineSensor(mid_pin)
        self.line_right = ICLineSensor(right_pin)

    @property
    def state(self):
        """返回传感器状态"""
        return (self.line_left.value, self.line_mid.value, self.line_right)


class ICInfraredSensor():
    """红外避障传感器"""

    def __init__(self, pin) -> None:
        

        pass


class InfraredSystem():
    """红外避障传感器系统"""

    def __init__(self, left_pin, right_pin) -> None:
        self.left = ICInfraredSensor(left_pin)
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

    def __init__(self, pin=None, initial_value=None, mid_tone=..., octaves=1, pin_factory=None):
        super().__init__(pin, initial_value, mid_tone, octaves, pin_factory)

        pass
    
    def play_song(self):
        """蜂鸣器演奏一首歌"""
        pass


class LED():
    """led 灯"""

    def __init__(self) -> None:
        pass
