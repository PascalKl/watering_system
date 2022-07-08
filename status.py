#!/usr/bin/env python
import RPi.GPIO as GPIO
import sendNotification
def get(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    status = GPIO.input(pin)
    if status == 1:
        print("keine Feuchtigkeit erkannt")
        GPIO.cleanup()
        #sendNotification.send("Blumen benötigen Wasser", "Deine Blumen benötigen Wasser, bitte schau´ demnächst mal nach!")
        return False

    else:
        print("Feuchtigkeit erkannt")
        GPIO.cleanup()
        return True
