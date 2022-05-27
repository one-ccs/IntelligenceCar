#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Done.py
#

import matplotlib.pyplot as plt
import cv2

def run():
    # 视频文件输入初始化
    filename = "/home/pi/Desktop/python代码/MP4/video.mp4"
    # camera = cv2.VideoCapture(filename)
    # 如果是摄像头的话
    camera = cv2.VideoCapture(0)  # 0表示默认摄像头
    # 视频文件输出参数设置
    out_fps = 30.0  # 输出文件的帧率
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # cv2.VideoWriter_fourcc返回的视频制式特定代码
    out1 = cv2.VideoWriter('/home/pi/Desktop/python代码/MP4/video2.mp4', fourcc, out_fps, (800, 400))  # 最后是视频宽高
    out2 = cv2.VideoWriter('/home/pi/Desktop/python代码/MP4/video3.mp4', fourcc, out_fps, (800, 400))
    # 初始化当前帧的前帧
    lastFrame = None
    # 遍历视频的每一帧
    while camera.isOpened():
        # 读取下一帧
        (ret, frame) = camera.read()
        # 如果不能抓取到一帧，说明我们到了视频的结尾
        if not ret:
            break
        # 调整该帧的大小
        frame = cv2.resize(frame, (800, 400), interpolation=cv2.INTER_CUBIC)
        # 结果转为灰度图
        gray_pic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_pic = cv2.GaussianBlur(gray_pic, (21, 21), 0)
        # 如果第一帧是None，对其进行初始化
        if lastFrame is None:
            lastFrame = gray_pic
            continue
        # 计算当前帧和前帧的不同，把两幅图的差的绝对值输出到另一幅图上面来
        frameDelta = cv2.absdiff(lastFrame, gray_pic)
        # 当前帧设置为下一帧的前帧
        lastFrame = gray_pic

        # 图像二值化
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        '''
        #去除图像噪声,先腐蚀再膨胀(形态学开运算)
        thresh=cv2.erode(thresh,None,iterations=1)
        thresh = cv2.dilate(thresh, None, iterations=2)
        '''
        # 阀值图像上的轮廓位置，在cv3中此函数的返回值才有三个
        # cv2.CHAIN_APPROX_SIMPLE，压缩垂直、水平、对角方向，只保留端点
        cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 遍历轮廓
        for c in cnts:
            # 忽略小轮廓，排除误差
            if cv2.contourArea(c) < 300:
                continue
            # 计算轮廓的边界框，在当前帧中画出该框
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 显示当前帧
        # cv2.imshow("frame", frame)
        plt.imshow(frame)
        plt.show()
        # cv2.imshow("frameDelta", frameDelta)
        # cv2.imshow("thresh", thresh)
        # 保存视频
        out1.write(frame)
        out2.write(frameDelta)
        # 如果q键被按下，跳出循环
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    # 清理资源并关闭打开的窗口
    out1.release()
    out2.release()
    camera.release()
    cv2.destroyAllWindows()

# run()
