#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import RPi.GPIO as GPIO
from datetime import datetime
import time

# 单位常量
TIME_TURN_DEG = 0.025  # 旋转 1 度的秒数
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
DISTANCE_TRIGGER_PIN = 20
# 寻线传感器针脚
LINES_LEFT_PIN = 13
LINES_MID_PIN = None
LINES_RIGHT_PIN = 26
# 蜂鸣器针脚常量
BUZZER_PIN = 11
# LED 针脚
GREEN_LED_PIN = 5
RED_LED_PIN = 6


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


def logger(info):
    """给日志加上时间"""
    print('[ {} ] : {}.'.format(str(datetime.now())[11:], info))


# 电机
def stop(t_time=3):
    logger('停止')
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(LEFT_REAR_PIN, False)
    GPIO.output(LEFT_FRONT_PIN, False)

    R_Motor.ChangeDutyCycle(0)
    GPIO.output(RIGHT_REAR_PIN, False)
    GPIO.output(RIGHT_FRONT_PIN, False)
    time.sleep(t_time)


def forward(speed=35, t_time=3):
    logger('前进')
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, False)
    GPIO.output(LEFT_FRONT_PIN, True)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, False)
    GPIO.output(RIGHT_FRONT_PIN, True)
    time.sleep(t_time)


def backward(speed=35, t_time=3):
    logger('后退')
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, True)
    GPIO.output(LEFT_FRONT_PIN, False)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, True)
    GPIO.output(RIGHT_FRONT_PIN, False)
    time.sleep(t_time)


def turn_left(speed=35, t_time=3):
    logger('左转')
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, True)
    GPIO.output(LEFT_FRONT_PIN, False)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, False)
    GPIO.output(RIGHT_FRONT_PIN, True)
    time.sleep(t_time)


def turn_right(speed=35, t_time=3):
    logger('右转')
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, False)
    GPIO.output(LEFT_FRONT_PIN, True)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, True)
    GPIO.output(RIGHT_FRONT_PIN, False)
    time.sleep(t_time)


# 蜂鸣器
def setup_buzzer():
    """初始化蜂鸣器"""
    logger('安装蜂鸣器')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    global buzzer_pwm
    buzzer_pwm = GPIO.PWM(BUZZER_PIN, 440)
    buzzer_pwm.start(50)


def clean_buzzer():
    """清理蜂鸣器资源"""
    logger('卸载蜂鸣器')
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

    for i in range(2):
        for i in range(1, len(song)):
            buzzer_pwm.ChangeFrequency(song[i])
            time.sleep(beat[i] * 0.5)
        time.sleep(1)


# 巡线传感器
def setup_lines():
    logger('安装巡线传感器')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LINES_LEFT_PIN, GPIO.IN)
    GPIO.setup(LINES_RIGHT_PIN, GPIO.IN)


def clean_lines():
    logger('卸载巡线传感器')
    GPIO.cleanup(LINES_LEFT_PIN)
    GPIO.cleanup(LINES_RIGHT_PIN)


def get_lines_state():
    ret_left = GPIO.input(LINES_LEFT_PIN)
    ret_right = GPIO.input(LINES_RIGHT_PIN)

    logger('获取巡线传感器状态 (左: {}, 右: {}).'.format(ret_left, ret_right))
    return (ret_left, ret_right)


def start_line():
    """开始巡线程序"""
    for i in range(99):
        lines_state = get_lines_state()

        if lines_state == (False, False):
            forward(t_time=0)
        elif lines_state == (True, False):
            turn_left(t_time=0)
        elif lines_state == (False, True):
            turn_right(t_time=0)
        else:
            stop(t_time=0)


# 红外避障传感器
def setup_infrareds():
    logger('安装红外避障传感器')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(INFRAREDS_LEFT_PIN, GPIO.IN)
    GPIO.setup(INFRAREDS_RIGHT_PIN, GPIO.IN)


def clean_infrareds():
    logger('卸载红外避障传感器')
    GPIO.cleanup(INFRAREDS_LEFT_PIN)
    GPIO.cleanup(INFRAREDS_RIGHT_PIN)


def get_infrared_state():
    ret_left = GPIO.input(INFRAREDS_LEFT_PIN)
    ret_right = GPIO.input(INFRAREDS_RIGHT_PIN)

    logger('获取红外避障传感器状态 (左: {}, 右: {}).'.format(ret_left, ret_right))
    return (ret_left, ret_right)


def start_infrared():
    """开始红外避障"""
    for i in range(99):
        infrared_state = get_infrared_state()

        if infrared_state == (True, True):
            forward()
        elif infrared_state == (True, False):
            turn_left()
        elif infrared_state == (False, True):
            turn_right()
        else:
            backward(t_time=0.5)
            turn_left(t_time=0.5)


# 超声波传感器
def setup_distance():
    logger('安装超声波传感器')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DISTANCE_ECHO_PIN, GPIO.IN)
    GPIO.setup(DISTANCE_TRIGGER_PIN, GPIO.OUT)


def clean_distance():
    logger('卸载超声波传感器')
    GPIO.cleanup(DISTANCE_ECHO_PIN)
    GPIO.cleanup(DISTANCE_TRIGGER_PIN)


def get_distance():
    """获取超声波传感器数值"""
    GPIO.output(DISTANCE_TRIGGER_PIN, 0)
    time.sleep(0.000002)

    GPIO.output(DISTANCE_TRIGGER_PIN, 1)
    time.sleep(0.00001)
    GPIO.output(DISTANCE_TRIGGER_PIN, 0)

    while GPIO.input(DISTANCE_ECHO_PIN) == 0:
        pass
    start_time = time.time()
    while GPIO.input(DISTANCE_ECHO_PIN) == 1:
        pass
    end_time = time.time()

    during = end_time - start_time
    distance = during * 340 / 2 * 100

    logger('获取超声波传感器数值: {} cm.'.format(distance))
    return distance


def start_distance():
    """开始超声波避障"""
    DIS = 20

    for i in range(99):
        dis = get_distance()

        if (dis < DIS) == True:
            while (dis < DIS) == True:
                backward(t_time=0.5)
                turn_right(t_time=0.5)

                dis = get_distance()
        else:
            forward(t_time=0)


def start_dis_inf():
    """超声波及红外混合避障"""
    DIS = 20

    for i in range(99):
        dis = get_distance()

        if (dis < DIS) == True:
            while (dis < DIS) == True:
                infrared_state = get_infrared_state()

                if infrared_state == (True, True):
                    logger('混合避障: 停止, 距离 {}'.format(dis))
                    stop()
                elif infrared_state == (True, False):
                    logger('混合避障: 左转, 距离 {}'.format(dis))
                    turn_left()
                elif infrared_state == (False, True):
                    logger('混合避障: 右转, 距离 {}'.format(dis))
                    turn_right()
                else:
                    logger('混合避障: 后退并左转, 距离 {}'.format(dis))
                    backward(t_time=0.5)
                    turn_left(t_time=0.5)

                dis = get_distance()
        else:
            forward(t_time=0)


# LED
def setup_led():
    logger('安装 led')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
    GPIO.setup(RED_LED_PIN, GPIO.OUT)


def clean_led():
    logger('卸载 led')
    GPIO.cleanup(GREEN_LED_PIN)
    GPIO.cleanup(RED_LED_PIN)


def set_green_led(state):
    if state == True:
        GPIO.output(GREEN_LED_PIN, 1)
        logger('打开绿色 led')
    else:
        GPIO.output(GREEN_LED_PIN, 0)
        logger('关闭绿色 led')


def set_red_led(state):
    if state == True:
        GPIO.output(RED_LED_PIN, 1)
        logger('打开红色 led')
    else:
        GPIO.output(RED_LED_PIN, 0)
        logger('关闭红色 led')


def start_led():
    """led 交替闪烁"""
    green = False
    red = True

    for i in range(10):
        set_green_led(not green)
        set_red_led(not red)

        green = not green
        red = not red
