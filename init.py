#!/usr/bin/env python
import time
import sendNotification
import status
import pump
import button
i = False
while i == True:
    status = status.get(18)
    while status == False:
        time.sleep(1)
        pump.turnOn(17)
        print("Pumpe eingeschaltet.")
        status = status.get(18)
    else:
        pump.turnOff(17)
        print("Pumpe ausgeschaltet.")
    if(button.getStatus(22) == 1):
        break
    time.sleep(5)