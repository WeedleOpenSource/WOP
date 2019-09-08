#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

Reed_AO_PIN = 11
LedPin = 16


def init():
	GPIO.setmode(GPIO.BOARD)	
	GPIO.setup(Reed_AO_PIN, GPIO.IN)
	GPIO.setup(LedPin, GPIO.OUT)
	
def loop():	
    while True:
        global digitalVal
        digitalVal = GPIO.input(Reed_AO_PIN)
        if(digitalVal == 0):
			print "Magnet detected!"
			GPIO.output(LedPin, GPIO.HIGH)
			time.sleep(0.2)
        else:
            GPIO.output(LedPin, GPIO.LOW)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		print 'The end !'
