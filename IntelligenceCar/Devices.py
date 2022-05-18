#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Sensors.py
#
#  Copyright 2022 ONE-CCS <ONE-CCS@ONE-CCS>
#
import RPI.GPIO as GPIO
import gpiozero as gz

import Adafruit_PCA9685
import cv2


class DistanceSensor(gz.DistanceSensor):
    """超声波传感器"""

    def __init__(self, echo=None, trigger=None):
        super().__init__(echo, trigger)

    def get_value(self) -> float:
        """返回测量的距离, 单位为厘米 (cm), 或使用 实例.distance 属性获取。"""
        return self.distance * 100


class LineSensor(gz.LineSensor):
    """巡线传感器"""

    def __init__(self, pin=None):
        super().__init__(pin)
        
    def get_value(self) -> float:
        """返回值接近 0 表示检测到黑色, 接近 1 表示接近白色。"""
        return self.value


class InfraredSensor():
    """红外避障传感器"""

    def __init__(self, pin=None) -> None:
        self.pin = pin

        if pin:
            GPIO.setwarnings(False)     # 关闭警告信息
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.IN)
        else:
            raise ValueError('初始化 class InfraredSensor 的参数 pin 为无效值。')

    @property
    def value(self) -> bool:
        """返回传感器检测值。"""
        return GPIO.input(self.pin)


class TonalBuzzer(gz.TonalBuzzer):
    """音调蜂鸣器"""
    DO = 261.6
    RE = 293.6
    MI = 329.6
    FA = 349.2
    SO = 392.0
    LA = 440.0
    SI = 493.8

    def __init__(self, pin=None):
        super().__init__(pin)

        pass

    def play_song(self, pitch_beat_list=()) -> None:
        """蜂鸣器演奏一首歌"""
        if not len(pitch_beat_list) % 2:
            raise ValueError("音阶-节拍表应该为偶数长度。")


class LEDBoard(gz.LEDBoard):
    """课同时空时控制多个 led"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pass


class Motor():
    """电机

    :参数 整型 p_pin:
        转速控制针脚 (pwm 针脚)。

    :参数 整型 f_pin:
        旋转方向控制引脚。
    """

    def __init__(self, p_pin, f_pin):
        self._speed = 50.0      # 转速占空比
        self._frequency = 100.0  # pwm 频率 (Hz)

        self.p_pin = p_pin
        self.f_pin = f_pin

        if p_pin and f_pin:
            GPIO.setwarnings(False)     # 关闭警告信息
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(p_pin, GPIO.OUT)
            GPIO.setup(f_pin, GPIO.OUT)
            self.pwm = GPIO.PWM(p_pin, self._frequency)
            self.pwm.start(0)
        else:
            raise ValueError('初始化 class Motor 的参数 p_pin 或 f_pin 为无效值。')

    def __del__(self):
        self.pwm.stop()

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, speed: float) -> None:
        """通过控制 pwm 占空比调节电机转速"""
        if speed < -100.0 or speed > 100.0:
            raise ValueError("无效的参数 speed, 应为 -100.0 到 +100.0 之间的数字。")
        else:
            self._speed = speed

    @property
    def frequency(self) -> float:
        """pwm 频率"""
        return self._frequency

    @frequency.setter
    def frequency(self, hz: float) -> None:
        self._frequency = hz
        self.pwm = GPIO.PWM(self.p_pin, hz)

    def forward(self) -> None:
        """前进"""
        self.pwm.ChangeDutyCycle(abs(self._speed))
        GPIO.output(self.f_pin, True)

    def backward(self) -> None:
        """后退"""
        self.pwm.ChangeDutyCycle(abs(self._speed))
        GPIO.output(self.f_pin, False)

    def stop(self) -> None:
        """停止"""
        self.pwm.ChangeDutyCycle(0)


class Camera():
    """摄像头"""

    def __init__(self, width=480, height=270) -> None:
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def __del__(self):
        self.camera.release()
        cv2.destroyAllWindows()

    def shoot(self) -> None:
        """拍摄一张照片"""
        _, frame = self.camera.read()
        return frame

    def upload(self) -> None:
        """上传照片"""
        pass

    def video(self) -> None:
        """实时录像"""
        pass


class Servo():
    """舵机"""

    def __init__(self, pin=None, frequency=50) -> None:
        self.pin = pin
        self._angle = 0

        if pin:
            self.servo = Adafruit_PCA9685.PCA9685()
            self.servo.set_pwm_freq(frequency)  # 设置 pwm 频率 (Hz)
            self.angle = 0

    @property
    def angle(self) -> int:
        return self._angle

    @angle.setter
    def angle(self, angle: int) -> None:
        """设置舵机的角度"""
        self._angle = angle
        angle = 4096 * ((angle * 11) + 500) / 20000
        self.servo.set_pwm(self.pin, 0, int(angle))


class PanTilt():
    """云台"""

    def __init__(self, vertical_pin=None, horizontal_pin=None) -> None:
        self.vertical = None
        self.horizontal = None

        if vertical_pin:
            self.vertical = Servo(vertical_pin)
        if horizontal_pin:
            self.horizontal = Servo(horizontal_pin)

    def move_up(self, deg: int) -> None:
        """向上转动指定度数。"""
        self.vertical.angle += deg

    def move_right(self, deg: int) -> None:
        """向右转动指定度数。"""
        self.horizontal.angle += deg

    def move_down(self, deg: int) -> None:
        """向下转动指定度数。"""
        self.vertical.angle -= deg

    def move_left(self, deg: int) -> None:
        """向左转动指定度数。"""
        self.horizontal.angle -= deg

    def orientation(self, coordinate={'x':None, 'y':None}) -> None:
        """以正前方为原点调整到指定位置。"""
        self.horizontal = coordinate['y']
        self.vertical = coordinate['x']
