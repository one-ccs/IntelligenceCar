#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  launch_server.py
#
from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("RaspberryPi.html")  # 返回主界面


@app.route("/horn", methods=["POST", "GET"])  # 返回轨迹界面
def horn():
    return render_template("Horn.html")


@app.route("/getHorn", methods=["POST", "GET"])  # 获取轨迹数据
def getHorn():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        # 用data的数据驱动小车
        return "OK"
    else:
        return "不支持该请求方式"


app.run()
