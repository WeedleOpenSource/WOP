#!/usr/bin/env python
import RPi.GPIO as GPIO

TrackPin = 11
LedPin   = 16 

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(TrackPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
	while True:
		if GPIO.input(TrackPin) == GPIO.LOW:
			GPIO.output(LedPin, GPIO.LOW)  # led on
		else:
			GPIO.output(LedPin, GPIO.HIGH) # led off

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  
		destroy()

