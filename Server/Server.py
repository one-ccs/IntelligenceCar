#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Server.py
#
from flask import Flask, request
from flask import render_template

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
        print(data)
        # 用data的数据驱动小车
        return "OK"
    else:
        return "不支持该请求方式"
