#!/usr/bin/env python

#
# This is a program for JoystickPS2 Module.
# This program depend on ADC0832 ADC chip.
#

import ADC0832
import RPi.GPIO as GPIO
import time

btn = 15	

xFlag = 0
yFlag = 0

def setup():
	ADC0832.setup()										# Setup ADC0832
	GPIO.setmode(GPIO.BOARD)							# Numbers GPIOs by physical location
	GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)	# Setup button pin as input an pull it up

def getResult():
	#get joystick result
	global xFlag, yFlag
	if ADC0832.getResult(1) == 0:
		xFlag = 1		#up
	if ADC0832.getResult(1) == 255:
		xFlag = 2		#down

	if ADC0832.getResult(0) == 0:
		yFlag = 1		#left
	if ADC0832.getResult(0) == 255:
		yFlag = 2		#right

	if GPIO.input(btn) == 0:
		print 'Button is pressed!'						# Button pressed

def loop():
	while True:
		getResult()
		if xFlag == 1:
			print 'up'
		elif xFlag == 2:
			print 'down'
		if yFlag == 1:
			print 'left'
		elif yFlag == 2:
			print 'right'

def destroy():
	GPIO.cleanup()										# Release resource

if __name__ == '__main__':								# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  	
		destroy()
