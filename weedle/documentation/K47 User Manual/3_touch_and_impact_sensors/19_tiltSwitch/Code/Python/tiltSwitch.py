#!/usr/bin/env python
import RPi.GPIO as GPIO

TiltPin = 11
LedPin  = 16

Led_status = 1

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(LedPin, GPIO.LOW) # Set LedPin low to off led


def loop():
	while True:
		if GPIO.input(TiltPin) == False:
			GPIO.output(LedPin, GPIO.HIGH)
		else:
			GPIO.output(LedPin, GPIO.LOW)

def destroy():
	GPIO.output(LedPin, GPIO.LOW)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

