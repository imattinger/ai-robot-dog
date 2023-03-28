# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
#front left
pwm0 = pwmio.PWMOut(board.PA00, duty_cycle=2 ** 15, frequency=50)
#front right
pwm1 = pwmio.PWMOut(board.PA01, duty_cycle=2 ** 15, frequency=50)
# back legs
pwm2 = pwmio.PWMOut(board.PA02, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.PE11, duty_cycle=2 ** 15, frequency=50)


# Create a servo object, my_servo.
FRONT_LEFT = servo.Servo(pwm0)
FRONT_RIGHT = servo.Servo(pwm1)
BACK_LEFT = servo.Servo(pwm2)
BACK_RIGHT = servo.Servo(pwm3)

print('-')

FRONT_LEFT.angle = 90
FRONT_RIGHT.angle = 90
BACK_LEFT.angle = 90
BACK_RIGHT.angle = 90

print('all legs at 90')


while True:
    for angle in range(25, 155, 5):  # 0 - 180 degrees, 5 degrees at a time.
        FRONT_LEFT.angle = angle
        BACK_LEFT.angle = angle
        FRONT_RIGHT.angle = angle
        BACK_RIGHT.angle = angle
        time.sleep(0.03)
    for angle in range(155, 25, -5): # 180 - 0 degrees, 5 degrees at a time.
        FRONT_LEFT.angle = angle
        BACK_LEFT.angle = angle
        FRONT_RIGHT.angle = angle
        BACK_RIGHT.angle = angle
        time.sleep(0.03)




'''
def moveLeg(

'''