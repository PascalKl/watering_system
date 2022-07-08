#!/usr/bin/env python
import RPi.GPIO as GPIO
def getStatus(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    status = GPIO.input(pin)
    return status