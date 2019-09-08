#!/usr/bin/env python
import RPi.GPIO as GPIO

ShockPin = 11
LedPin   = 16

Led_status = 0

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(ShockPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	

def swLed(ev=None):
	global Led_status
	Led_status = not Led_status
	GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
        print "led: " + ("on" if Led_status else "off")

def loop():
	GPIO.add_event_detect(ShockPin, GPIO.FALLING, callback=swLed, bouncetime=200) # wait for falling
	while True:
		pass   # Don't do anything

def destroy():
	GPIO.output(LedPin, GPIO.LOW)      # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

