from math import sqrt

from IntelligenceCar.Car import Car
from IntelligenceCar.Devices import ICTonalBuzzer


def base_demo(car: Car) -> None:
    """智能小车基础功能演示"""
    # 移动演示
    car.forward(10)
    car.backward(10)
    car.turn_left(360)
    car.turn_right(360)
    # 蜂鸣器演示
    car.buzzer.play(ICTonalBuzzer.DO)
    car.buzzer.play(ICTonalBuzzer.RE)
    car.buzzer.play(ICTonalBuzzer.MI)
    car.buzzer.play(ICTonalBuzzer.FA)
    car.buzzer.play(ICTonalBuzzer.SO)
    car.buzzer.play(ICTonalBuzzer.LA)
    car.buzzer.play(ICTonalBuzzer.SI)
    # led 演示
    
    # 超声波演示
    # 寻迹参数显示
    # 红外避障参数演示
    # 摄像头云台运动演示
    # 超声波伺服器运动演示


def sport_demo(car: Car) -> None:
    """智能小车运动演示"""
    # 走一个正方形
    for i in range(4):
        # 前进 100 cm
        car.forward(100)
        # 右转 90°
        car.turn_right(90)

    # 走一个 "又" 字
    car.turn_right(45)
    car.forward(100 * sqrt(2))
    car.turn_right(45)
    car.backward(100)
    car.turn_right(45)
    car.forward(100)

    # 回到起点
    car.turn_left(225)
    car.forward(100)
    car.turn_left(270)


def line_demo(car: Car) -> None:
    """智能小车巡线演示"""
    for i in range(500):
        if car.lines.state == (False, True, False):
            # 在中心线 直行
            car.forward(4)
        elif car.lines.state == (True, False, False):
            # 偏右 向左转
            car.turn_left(15)
        elif car.lines.state == (False, False, True):
            # 偏左 向右转
            car.turn_right(15)


def infrared_demo(car: Car) -> None:
    """智能小车红外避障演示"""
    pass


def distance_demo(car: Car) -> None:
    """智能小车超声波避障演示"""
    min_distance = 20

    while(True):
        if car.distance.value < min_distance:
            car.backward(4)
            car.turn_left(30)


def automatic_track_demo(car: Car) -> None:
    """智能小车自动寻物演示"""
    pass
