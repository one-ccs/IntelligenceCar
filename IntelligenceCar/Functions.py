#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import RPi.GPIO as GPIO
import time

# 单位常量
TIME_TURN_DEG = 0.07  # 旋转 1 度的秒数
TIME_STRAIGHT = 0.02  # 直行 1 单位的秒数

# 电机针脚常量
LEFT_FRONT_PIN = 22  # AIN1
LEFT_REAR_PIN = 27   # AIN2
LEFT_PWM_PIN = 18    # PWMA
RIGHT_FRONT_PIN = 25  # BIN1
RIGHT_REAR_PIN = 24  # BIN2
RIGHT_PWM_PIN = 23   # PWMB
# 红外避障传感器针脚
INFRAREDS_LEFT_PIN = 12
INFRAREDS_RIGHT_PIN = 16
# 超声波传感器针脚
DISTANCE_ECHO_PIN = 21
DISTANCE_TRIGGER_PIN = 21
# 寻线传感器针脚
LINES_LEFT_PIN = 13
LINES_MID_PIN = None
LINES_RIGHT_PIN = 26
# 蜂鸣器针脚常量
BUZZER_PIN = 11
# LED 针脚
GREEN_LED = 5
RED_LED = 6


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LEFT_FRONT_PIN, GPIO.OUT)
GPIO.setup(LEFT_REAR_PIN, GPIO.OUT)
GPIO.setup(LEFT_PWM_PIN, GPIO.OUT)
L_Motor = GPIO.PWM(LEFT_PWM_PIN, 100)
L_Motor.start(0)

GPIO.setup(RIGHT_FRONT_PIN, GPIO.OUT)
GPIO.setup(RIGHT_REAR_PIN, GPIO.OUT)
GPIO.setup(RIGHT_PWM_PIN, GPIO.OUT)
R_Motor = GPIO.PWM(RIGHT_PWM_PIN, 100)
R_Motor.start(0)


# 电机
def stop(t_time=3):
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(LEFT_REAR_PIN, False)
    GPIO.output(LEFT_FRONT_PIN, False)

    R_Motor.ChangeDutyCycle(0)
    GPIO.output(RIGHT_REAR_PIN, False)
    GPIO.output(RIGHT_FRONT_PIN, False)
    time.sleep(t_time)


def forward(speed=35, t_time=3):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, False)
    GPIO.output(LEFT_FRONT_PIN, True)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, False)
    GPIO.output(RIGHT_FRONT_PIN, True)
    time.sleep(t_time)


def backward(speed=35, t_time=3):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, True)
    GPIO.output(LEFT_FRONT_PIN, False)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, True)
    GPIO.output(RIGHT_FRONT_PIN, False)
    time.sleep(t_time)


def turn_left(speed=35, t_time=3):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, True)
    GPIO.output(LEFT_FRONT_PIN, False)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, False)
    GPIO.output(RIGHT_FRONT_PIN, True)
    time.sleep(t_time)


def turn_right(speed=35, t_time=3):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, False)
    GPIO.output(LEFT_FRONT_PIN, True)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, True)
    GPIO.output(RIGHT_FRONT_PIN, False)
    time.sleep(t_time)


def run1(speed=35, t_time=3, arg=False):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, arg)
    time.sleep(t_time)


def run1_1(speed=35, t_time=3, arg=True):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, arg)
    time.sleep(t_time)


def run2(speed=35, t_time=3, arg=False):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_FRONT_PIN, arg)
    time.sleep(t_time)


def run2_2(speed=35, t_time=3, arg=True):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_FRONT_PIN, arg)
    time.sleep(t_time)


def run3(speed=35, t_time=3, arg=False):
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, arg)
    time.sleep(t_time)


def run3_3(speed=35, t_time=3, arg=True):
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, arg)
    time.sleep(t_time)


def run4(speed=35, t_time=3, arg=False):
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_FRONT_PIN, arg)
    time.sleep(t_time)


def run4_4(speed=35, t_time=3, arg=True):
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_FRONT_PIN, arg)
    time.sleep(t_time)


# 蜂鸣器
def setup_buzzer():
    """初始化蜂鸣器"""
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    global buzzer_pwm
    buzzer_pwm = GPIO.PWM(BUZZER_PIN, 440)
    buzzer_pwm.start(50)


def clean_buzzer():
    """清理蜂鸣器资源"""
    buzzer_pwm.stop()
    GPIO.output(buzzer_pwm, 1)
    GPIO.cleanup(BUZZER_PIN)


def play_song():
    """使用蜂鸣器演奏一首歌曲"""
    CL = [0, 131, 147, 165, 175, 196, 211, 248]  # 低 C 音符频率
    CM = [0, 262, 294, 330, 350, 393, 441, 495]  # 中 C 音符频率
    CH = [0, 525, 589, 661, 700, 786, 882, 990]  # 高 C 音符频率
    song = [
        CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6],
        CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
        CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
        CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]
    ]  # 音谱
    beat = [
        1, 1, 3, 1, 1, 3, 1, 1,
        1, 1, 1, 1, 1, 1, 3, 1,
        1, 3, 1, 1, 1, 1, 1, 1,
        1, 2, 1, 1, 1, 1, 1, 1,
        1, 1, 3
    ]  # 八分之一拍

    setup_buzzer()
    for i in range(2):
        for i in range(1, len(song)):
            buzzer_pwm.ChangeFrequency(song[i])
            time.sleep(beat[i] * 0.5)
        time.sleep(1)
    clean_buzzer()


# 巡线传感器
def setup_line():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.setup(LINES_LEFT_PIN, GPIO.IN)
    GPIO.setup(LINES_RIGHT_PIN, GPIO.IN)
