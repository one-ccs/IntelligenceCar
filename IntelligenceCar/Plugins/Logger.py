#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Logger.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
from datetime import datetime


class Logger():
    """包含常用日志函数"""

    def __init__(self) -> None:
        pass

    def log(self, info, level=0):
        print('[ {} ] : <class {}> {}.'.format(
            str(datetime.now())[11:],
            self.__class__.__name__,
            info)
        )
