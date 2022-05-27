#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TonalBuzzer.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import gpiozero as gz

class TonalBuzzer(gz.TonalBuzzer):
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

    def play_song(self, pitch_beat_list=()):
        """蜂鸣器演奏一首歌"""
        if not len(pitch_beat_list) % 2:
            raise ValueError("音阶-节拍表应该为偶数长度。")
