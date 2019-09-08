#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import sys
from time import sleep
from Adafruit_CCS811 import *

def readCO2():
    
    try:
        print ("== IN READ CO2 IN THE BOX == ")
#        GPIO.cleanup() 
        ccs =  Adafruit_CCS811()
#        BME280_REGISTER_SOFTRESET = 0xE0
#        self._device.write8(BME280_REGISTER_SOFTRESET, 0xB6)
        while not ccs.available():
            pass
        temp = ccs.calculateTemperature()
        ccs.tempOffset = temp - 25.0

        while(1):
            if ccs.available():
                temp = ccs.calculateTemperature()
                if not ccs.readData():
                  #print "CO2: ", ccs.geteCO2(), "ppm, TVOC: ", ccs.getTVOC(), " temp: ", temp
                    return ccs.geteCO2()

                else:
                  print "#####   ERROR IN READING CO2! ######"
                  return -100
                  while(1):
                    pass
            sleep(2)
        
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            GPIO.cleanup()                     # Release resource

def destroy(pin):
    GPIO.cleanup()                     # Release resource


if __name__ == '__main__':             # Program start from here
    try:
        CO2 = readCO2()
        print ("CO2: " + str(CO2))
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy(5)



