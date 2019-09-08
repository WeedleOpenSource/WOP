#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LaserPin = 11    # pin11
LedPin = 16

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LaserPin, GPIO.OUT)   # Set LaserPin's mode is output
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	

def loop():
	while True:
		print '...LaserPin on'
		GPIO.output(LaserPin, GPIO.HIGH)  # LaserPin on
		GPIO.output(LedPin, GPIO.HIGH)
		time.sleep(0.5)
		print 'LaserPin off...'
		GPIO.output(LaserPin, GPIO.LOW) # LaserPin off
		GPIO.output(LedPin, GPIO.LOW)
		time.sleep(0.5)

def destroy():
	GPIO.output(LaserPin, GPIO.LOW)     # LaserPin off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
