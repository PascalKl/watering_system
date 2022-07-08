#!/usr/bin/env python
import RPi.GPIO as GPIO
def turnOn(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
    GPIO.output(pin, 1)
def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
    GPIO.output(pin, 0)
