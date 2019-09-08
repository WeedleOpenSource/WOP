#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin   = 16
TouchPin = 11


def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(LedPin, GPIO.LOW) # Set LedPin low to off led

def loop():
	while True:
		if GPIO.input(TouchPin) == GPIO.HIGH:
			print 'touched!'
			GPIO.output(LedPin, GPIO.HIGH)  # led on
                        time.sleep(0.2)
		else:	
			GPIO.output(LedPin, GPIO.LOW) # led off

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  
		destroy()

