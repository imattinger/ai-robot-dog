# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm0 = pwmio.PWMOut(board.PA00, duty_cycle=2 ** 15, frequency=50)
pwm1 = pwmio.PWMOut(board.PA01, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.PA02, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.PE11, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
FRONT_RIGHT = servo.Servo(pwm0)
FRONT_LEFT = servo.Servo(pwm1)
BACK_RIGHT = servo.Servo(pwm2)
BACK_LEFT = servo.Servo(pwm3)

print('-')

def setAll(angle):
    FRONT_LEFT.angle = angle
    BACK_LEFT.angle = angle
    FRONT_RIGHT.angle = 180 - angle
    BACK_RIGHT.angle = 180 - angle

def setAllNoAdjust(angle):
    FRONT_LEFT.angle = angle
    BACK_LEFT.angle = angle
    FRONT_RIGHT.angle = angle
    BACK_RIGHT.angle = angle
    
def setFront(angle):
    FRONT_LEFT.angle = angle
    FRONT_RIGHT.angle = 180 - angle

def setBack(angle):
    BACK_LEFT.angle = angle
    BACK_RIGHT.angle = 180 - angle


def standingPose():
    setAll(90)
    
def sittingPose():
    setBack(0)

def lyingPose():
    setFront(0)
    setBack(0)

# Sitting/lying -> standing makes robot jump
# FIX - this might not work well if front or
# back legs pointing opp from each other
def getUpSlowly():
    front_start = FRONT_LEFT.angle
    for angle in range(front_start, 90, 5):
        setFront(angle)
        if BACK_LEFT.angle < angle - 10:
            setBack(angle-10)
        time.sleep(0.05)
    standingPose()
    


def motorTest():
    while True:
        for angle in range(25, 155, 5):  # 0 - 180 degrees, 5 degrees at a time.
            setAllNoAdjust(angle)
            time.sleep(0.03)
        for angle in range(155, 25, -5): # 180 - 0 degrees, 5 degrees at a time.
            setAllNoAdjust(angle)
            time.sleep(0.03)

'''
lyingPose()
time.sleep(2)
getUpSlowly()
'''

def setLeftDiag(angle):
    FRONT_LEFT.angle = angle
    BACK_RIGHT.angle = 180 - angle

def setRightDiag(angle):
    FRONT_RIGHT.angle = 180 - angle
    BACK_LEFT.angle = angle

# Based on what I think is a horse trot?
# Work in progress - not entirely sure
# this is possible with no knees
def trotWalk():
    standingPose()
    while True: 
        setLeftDiag(45)
        setRightDiag(135)
        standingPose()
        time.sleep(0.5)
        setRightDiag(45)
        setLeftDiag(135)
        standingPose()



'''
Problem with current design - robot is much
heavier in the back (this makes it hard to
walk forward when it has no knees). The code
below makes robot walk backwards.
'''
def shuffleRun():
    while True:
        standingPose()
        for angle in range(90, 135, 5):
            setBack(angle)
            time.sleep(0.02)
        for angle in range(90, 50, -5):
            setFront(angle)
            time.sleep(0.02)
        for angle in range(135, 90, -5):
            setBack(angle)
            time.sleep(0.02)
    

# shuffleRun()


def demoPoses():
    standingPose()
    time.sleep(2)
    sittingPose()
    time.sleep(2)
    lyingPose()
    time.sleep(2)
    getUpSlowly()


