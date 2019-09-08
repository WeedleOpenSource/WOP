#!/usr/bin/env python
import RPi.GPIO as GPIO

ObstaclePin = 11
LedPin = 16

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(LedPin, GPIO.OUT)
		
def loop():
	while True:
		if (0 == GPIO.input(ObstaclePin)):
		    print "Barrier is detected !"
                    GPIO.output(LedPin, True)
                else:
                    GPIO.output(LedPin, False)
			

def destroy():
	GPIO.cleanup()                      # Release resource

if __name__ == '__main__':     			# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  
		destroy()

