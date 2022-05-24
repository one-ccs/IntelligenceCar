#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Server.py
#
from flask import Flask, request, Response
from flask import render_template
import cv2

from os import path as op
from sys import path as sp
BASE_DIR = op.dirname(op.dirname(op.abspath(__file__))) #当前程序上上一级目录，这里为mycompany
sp.append(BASE_DIR) #添加环境变量
from IntelligenceCar.Functions import *

ic_server = Flask(__name__)


class VideoCamera(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # 在这里处理视频帧
        cv2.putText(image, "hello", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0))
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


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

        if towards != "后":
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


@ic_server.route('/Vedio')
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('Vedio.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@ic_server.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@ic_server.route("/ultrasonic")
def ultrasonic():
    return render_template("ultrasonic.html")


@ic_server.route("/showDistance", methods=['POST', 'GET'])
def showDistance():
    # dis=距离
    dis = 0
    return str(dis)


ic_server.run()
