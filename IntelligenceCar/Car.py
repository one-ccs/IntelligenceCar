#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Car.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import RPi.GPIO as GPIO
from time import sleep

from IntelligenceCar.Devices.DistanceSensor import DistanceSensor
from IntelligenceCar.Devices.LEDBoard import LEDBoard
from IntelligenceCar.Devices.TonalBuzzer import TonalBuzzer
from IntelligenceCar.Devices.Servo import Servo
from IntelligenceCar.Devices.PanTilt import PanTilt
from IntelligenceCar.Plugins.Logger import Logger
from IntelligenceCar.Plugins.MotorSystem import MotorSystem
from IntelligenceCar.Plugins.InfraredSystem import InfraredSystem
from IntelligenceCar.Plugins.LineSystem import LineSystem


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
BUZZER_PIN = 17
# LED 针脚
GREEN_LED_PIN = 5
RED_LED_PIN = 6
# 舵机针脚
DISTANCE_SERVO_PIN = 0
CAMERA_HORIZONTAL_SERVO_PIN = 1
CAMERA_VERTICAL_SERVO_PIN = 2


class Car(Logger):
    """智能小车

    :参数 整型元组 wheels_pin:
        四个电机的针脚 (
            (左电机 1, 左电机 2), 左 pwm,
            (右电机 1, 右电机 2), 右 pwm
        )。

    :参数 整型元组 infrareds_pin:
        红外避障传感器针脚 (左, 右)。

    :参数 整型元组 distance_pin:
        超声波 (距离) 传感器针脚 (echo, trigger)。

    :参数 整型元组 lines_pin:
        寻线传感器针脚 (左, 中, 右)。

    :参数 整型 buzzer_pin:
        蜂鸣器针脚。
    """
    STEER_TIME = 0.025    # 车子旋转 1° 需要的秒数
    STRAIGHT_TIME = 0.02  # 车子直行一单位 1cm 需要的秒数

    def __init__(
        self,
        wheels_pin=((None, None), None, (None, None), None),
        infrareds_pin=(None, None),
        distance_pin=(None, None),
        lines_pin=(None, None, None),
        leds_pin=(None, None),
        buzzer_pin=None,
        distance_servo_pin=None,
        camera_servos_pin=(None, None)
    ):
        self.wheels = None
        self.infrareds = None
        self.distance = None
        self.lines = None
        self.lights = None
        self.buzzer = None
        self.distance_servo = None
        self.camera_pantilt = None

        if wheels_pin != ((None, None), None, (None, None), None):
            # 车轮系统
            self.log('安装车轮系统, 针脚: {}'.format(wheels_pin))
            self.wheels = MotorSystem(wheels_pin)
        if infrareds_pin != (None, None):
            # 红外避障
            self.log('安装红外避障系统, 针脚: {}'.format(infrareds_pin))
            self.infrareds = InfraredSystem(infrareds_pin[0], infrareds_pin[1])
        if distance_pin != (None, None):
            # 超声波
            self.log('安装超声波模块, 针脚: {}'.format(distance_pin))
            self.distance = DistanceSensor(distance_pin[0], distance_pin[1])
        if lines_pin != (None, None, None):
            # 巡线
            self.log('安装巡线系统, 针脚: {}'.format(lines_pin))
            self.lines = LineSystem(lines_pin[0], lines_pin[1], lines_pin[2])
        if leds_pin != (None, None):
            # LED
            self.log('安装 LED, 针脚: {}'.format(leds_pin))
            self.lights = LEDBoard(leds_pin[0], leds_pin[1], pwm=True)
        if buzzer_pin != None:
            # 音调蜂鸣器
            self.log('安装蜂鸣器, 针脚: {}'.format(buzzer_pin))
            self.buzzer = TonalBuzzer(buzzer_pin)
        if distance_servo_pin != None:
            self.log('安装超声波传感器伺服, 针脚: {}'.format(distance_servo_pin))
            self.distance_servo = Servo(distance_servo_pin)
        if camera_servos_pin != (None, None):
            self.log('安装摄像头云台伺服, 针脚: {}'.format(camera_servos_pin))
            self.camera_pantilt = PanTilt(
                camera_servos_pin[0], camera_servos_pin[1]
            )

    def stop(self):
        """停止"""
        self.log('停止')
        self.wheels.stop()

    def forward(self, distance=10):
        """
        向前指定单位 1cm 的距离。

        :参数 整型 deg:
            要选择的度数。
        """
        self.log('前进 {} 单位, {} 秒'.format(
            distance, Car.STRAIGHT_TIME * distance))
        self.wheels.forward()
        sleep(Car.STRAIGHT_TIME * distance)
        self.wheels.stop()

    def backward(self, distance=10):
        """
        向前指定单位 1cm 的距离。

        :参数 整型 deg:
            要选择的度数。
        """
        self.log('后退 {} 单位, {} 秒'.format(
            distance, Car.STRAIGHT_TIME * distance))
        self.wheels.backward()
        sleep(Car.STRAIGHT_TIME * distance)
        self.wheels.stop()

    def turn_left(self, deg=10):
        """
        向左旋转指定度数。

        :参数 整型 deg:
            要选择的度数。
        """
        self.log('向左旋转 {} 单位, {} 秒'.format(
            deg, Car.STRAIGHT_TIME * deg))
        self.wheels.turn_left()
        sleep(Car.STEER_TIME * deg)
        self.wheels.stop()

    def turn_right(self, deg=10):
        """
        向右旋转指定度数。

        :参数 整型 deg:
            要选择的度数。
        """
        self.log('向右旋转 {} 单位, {} 秒'.format(
            deg, Car.STRAIGHT_TIME * deg))
        self.wheels.turn_right()
        sleep(Car.STEER_TIME * deg)
        self.wheels.stop()

    def turn_both_light_on(self):
        self.lights.on()

    def turn_both_light_off(self):
        self.lights.off()

    def turn_light_alternate(self):
        """交替闪烁"""
        self.log('交替闪烁 led')
        for i in range(8):
            self.lights.value = (1, 0)
            sleep(0.5)
            self.lights.value = (0, 1)
            sleep(0.5)

    def turn_bearth_light(self):
        """呼吸灯"""
        self.log('led 呼吸灯')
        for j in range(5):
            for i in range(0, 100, 10):
                self.lights.value = (i / 100, i / 100)
                sleep(0.1)
            for i in range(100, 0, -10):
                self.lights.value = (i / 100, i / 100)
                sleep(0.1)

    def play_song(self):
        """蜂鸣器演奏歌曲"""
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

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUZZER_PIN, GPIO.OUT)
        buzzer_pwm = GPIO.PWM(BUZZER_PIN, 440)
        buzzer_pwm.start(50)

        for i in range(2):
            for i in range(1, len(song)):
                buzzer_pwm.ChangeFrequency(song[i])
                sleep(beat[i] * 0.5)
            sleep(1)

        buzzer_pwm.stop()
        GPIO.output(buzzer_pwm, 1)
        GPIO.cleanup(BUZZER_PIN)

    def get_lines_state(self):
        """返回巡线传感器状态"""
        ret = self.lines.state

        self.log('获取巡线系统状态 {}'.format(ret))

        return ret

    def start_line(self):
        """开始巡线程序"""
        for i in range(999):
            lines_state = self.get_lines_state()

            if lines_state == (False, False):
                self.forward()
            elif lines_state == (True, False):
                self.turn_left()
            elif lines_state == (False, True):
                self.turn_right()
            else:
                self.stop()

    def get_infrared_state(self):
        """返回红外避障传感器状态"""
        ret = self.infrareds.state

        self.log('获取红外避障系统状态 {}'.format(ret))

        return ret

    def start_infrared(self):
        """开始红外避障程序"""
        for i in range(99):
            infrared_state = self.get_infrared_state()

            if infrared_state == (True, True):
                self.forward()
            elif infrared_state == (True, False):
                self.turn_left()
            elif infrared_state == (False, True):
                self.turn_right()
            else:
                self.backward(50)
                self.turn_left(50)

    def get_distance(self):
        """获取超声波传感器数值, 单位 cm."""
        ret = self.distance.get_value()
        self.log('获取超声波传感器数值 {}'.format(ret))

        return ret

    def start_distance(self):
        """开始超声波避障程序"""
        DIS = 20

        for i in range(99):
            dis = self.get_distance()

            if (dis < DIS) == True:
                while (dis < DIS) == True:
                    self.backward(50)
                    self.turn_right(50)

                    dis = self.get_distance()
            else:
                self.forward(50)

    def start_dis_inf(self):
        """超声波及红外混合避障"""
        DIS = 20

        for i in range(99):
            dis = self.get_distance()

            if (dis < DIS) == True:
                while (dis < DIS) == True:
                    infrared_state = self.get_infrared_state()

                    if infrared_state == (True, True):
                        self.log('混合避障: 停止, 距离 {}'.format(dis))
                        self.stop()
                    elif infrared_state == (True, False):
                        self.log('混合避障: 左转, 距离 {}'.format(dis))
                        self.turn_left()
                    elif infrared_state == (False, True):
                        self.log('混合避障: 右转, 距离 {}'.format(dis))
                        self.turn_right()
                    else:
                        self.log('混合避障: 后退并左转, 距离 {}'.format(dis))
                        self.backward(50)
                        self.turn_left(50)

                    dis = self.get_distance()
            else:
                self.forward(50)

    def set_servo(self, deg=0):
        """设置超声波传感器伺服角度"""
        print(self.distance_servo.min())
        sleep(2)
        self.distance_servo.angle = 90
        sleep(2)
        print(self.distance_servo.max())
        sleep(2)

    def set_pantilt(self, horizontal_deg=0, vertical_deg=0):
        """设置摄像头云台角度"""
        pass
