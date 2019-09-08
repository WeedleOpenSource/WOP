#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pin_R = 10

def setup():
	GPIO.setmode(GPIO.BOARD)			# Numbers GPIOs by physical location
	GPIO.setup(pin_R, GPIO.OUT)

try:
	setup()
	while True:
            GPIO.output(pin_R, GPIO.HIGH)				
except KeyboardInterrupt:
	GPIO.cleanup()

