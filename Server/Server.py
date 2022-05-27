#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Server.py
#
from flask import Flask, request, Response, render_template
import random
import cv2

from os import path as op
from sys import path as sp
sp.append(op.dirname(op.dirname(op.abspath(__file__))))  # 添加环境变量为上级目录
from IntelligenceCar.Functions import *

ic_server = Flask(__name__, static_folder='./static')
global_car = None


class VideoCamera(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture(0)
        self.camera_width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.camera_height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.video_width = int(self.camera_width)
        self. video_height = int(self.camera_height)
        # 设置相机宽度
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_width)
        # 设置相机高度
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_height)
        self.video_fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv2.VideoWriter(
            r'./static/output.avi', self.video_fourcc, 30, (self.video_width, self.video_height))

    def __del__(self):
        self.video.release()

    def get_frameAndVideo(self):
        success, image = self.video.read()
        # 在这里处理视频帧
        cv2.putText(image, "hello", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0))
        self.video_writer.write(image)
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_frame(self):
        success, image = self.video.read()
        # 在这里处理视频帧
        cv2.putText(image, "hello", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0))
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


@ic_server.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


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

        if towards != 1:
            # 转向 180 度
            turn_left(t_time=TIME_TURN_DEG * 180)

        for line in hData:
            if line[2] == -1:  # 左转
                turn_left(t_time=TIME_TURN_DEG * line[0])
                # global_car.turn_left(line[0])
            elif line[2] == 1:  # 右转
                turn_right(t_time=TIME_TURN_DEG * line[0])
                # global_car.turn_right(line[0])
            else:  # 直行
                forward(t_time=TIME_STRAIGHT * line[1])
                # global_car.forward(line[1])

        stop()
        # global_car.stop()

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


def gen1(camera):
    while True:
        frame = camera.get_frameAndVideo()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@ic_server.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@ic_server.route('/video_feed1')  # 这个地址返回视频流响应
def video_feed1():
    return Response(gen1(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@ic_server.route("/ultrasonic")
def ultrasonic():
    return render_template("ultrasonic.html")


@ic_server.route("/showDistance", methods=['POST', 'GET'])
def showDistance():
    # dis=get_distance()
    dis = global_car.get_distance()
    dis = random.random()
    return str(dis)


@ic_server.route("/LED")
def LED():
    return "OK"


@ic_server.route("/buzzer")
def Buzzer():
    return "buzzer"


@ic_server.route("/monitor")
def monitor():
    return render_template("monitor.html")


@ic_server.route("/ctrl", methods=['POST', 'GET'])
def ctrl():
    if request.method == "POST":
        data = request.get_json()
        t = data['ctrl']
        # forward(t_time=1.5)
        global_car.forward(1.5)
        # backward(t_time=1.5)
        global_car.backward(1.5)
        # turn_left(t_time=0.3)
        global_car.turn_left(0.3)
        # turn_right(t_time=0.3)
        global_car.turn_right(0.3)
    else:
        return "No"


@ic_server.route("/tracing")
def tracing():

    return "tracing"


def run(car):
    """启动服务器"""
    global global_car

    global_car = car
    ic_server.run(host='0.0.0.0')
