#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Server.py
#
from flask import Flask, request
from flask import render_template

from sys import path
path.append(__file__[:-17])
from IntelligenceCar.Functions import *

ic_server = Flask(__name__)


@ic_server.route("/")
def main():
    return render_template("RaspberryPi.html")  # 返回主界面


@ic_server.route("/horn", methods=["POST", "GET"])  # 返回轨迹界面
def horn():
    return render_template("Horn.html")


@ic_server.route("/getHorn", methods=["POST", "GET"])  # 获取轨迹数据
def getHorn():
    if request.method == "POST":
        data = request.get_json()
        lines = data['data']
        towards = data['toward']
        hData = []
        for i in lines:
            t1 = [i[0], 0, i[2]]
            hData.append(t1)
            t2 = [0, i[1], 0]
            hData.append(t2)

        if towards == 1:
            # 转向 180 度
            turn_left(t_time=TIME_TURN_DEG * 180)

        for line in hData:
            if line[2] == -1:  # 左转
                turn_left(t_time=TIME_TURN_DEG * line[0])
            elif line[2] == 1:  # 右转
                turn_right(t_time=TIME_TURN_DEG * line[0])
            else:  # 直行
                forward(t_time=TIME_STRAIGHT * line[1])

        stop()

        return "OK"
    else:
        return "不支持该请求方式"


ic_server.run()
