#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import RPi.GPIO as GPIO
import time

LEFT_FRONT_PIN = 22  # AIN1
LEFT_REAR_PIN = 27   # AIN2
LEFT_PWM_PIN = 18    # PWMA

RIGHT_FRONT_PIN = 25  # BIN1
RIGHT_REAR_PIN = 24  # BIN2
RIGHT_PWM_PIN = 23   # PWMB


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


def stop(t_time=3):
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(LEFT_REAR_PIN, False)
    GPIO.output(LEFT_FRONT_PIN, False)

    R_Motor.ChangeDutyCycle(0)
    GPIO.output(RIGHT_REAR_PIN, False)
    GPIO.output(RIGHT_FRONT_PIN, False)
    time.sleep(t_time)


def forward(speed=30, t_time=3):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, False)
    GPIO.output(LEFT_FRONT_PIN, True)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, False)
    GPIO.output(RIGHT_FRONT_PIN, True)
    time.sleep(t_time)


def backward(speed=30, t_time=3):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, True)
    GPIO.output(LEFT_FRONT_PIN, False)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, True)
    GPIO.output(RIGHT_FRONT_PIN, False)
    time.sleep(t_time)


def turn_left(speed=30, t_time=3):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, True)
    GPIO.output(LEFT_FRONT_PIN, False)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, False)
    GPIO.output(RIGHT_FRONT_PIN, True)
    time.sleep(t_time)


def turn_right(speed=30, t_time=3):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, False)
    GPIO.output(LEFT_FRONT_PIN, True)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, True)
    GPIO.output(RIGHT_FRONT_PIN, False)
    time.sleep(t_time)


def run1(speed=30, t_time=3, arg=False):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, arg)
    time.sleep(t_time)


def run1_1(speed=30, t_time=3, arg=True):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_REAR_PIN, arg)
    time.sleep(t_time)


def run2(speed=30, t_time=3, arg=False):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_FRONT_PIN, arg)
    time.sleep(t_time)


def run2_2(speed=30, t_time=3, arg=True):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(LEFT_FRONT_PIN, arg)
    time.sleep(t_time)


def run3(speed=30, t_time=3, arg=False):
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, arg)
    time.sleep(t_time)


def run3_3(speed=30, t_time=3, arg=True):
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_REAR_PIN, arg)
    time.sleep(t_time)


def run4(speed=30, t_time=3, arg=False):
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_FRONT_PIN, arg)
    time.sleep(t_time)


def run4_4(speed=30, t_time=3, arg=True):
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(RIGHT_FRONT_PIN, arg)
    time.sleep(t_time)
