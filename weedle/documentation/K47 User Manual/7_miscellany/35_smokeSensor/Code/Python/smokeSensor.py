#!/usr/bin/env python

#
# This is a program for MQ-2 Gas Sensor Module.
# It could detect danger gas and smokes.
# This program depends on ADC0832 ADC chip. Follow 
# the instruction book to connect the module and 
# ADC0832 to your Raspberry Pi.
#


import RPi.GPIO as GPIO
import ADC0832
import time

SensorDoPin = 15
LedPin = 16					


def setup():
	GPIO.setmode(GPIO.BOARD)		# Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)		
	GPIO.setup(SensorDoPin, GPIO.IN)
	ADC0832.setup()					

def loop():
    while True:
	    analogVal = ADC0832.getResult(0)	# Get analog value from ADC0832
	    print analogVal					# Print analog value
							
	    if not GPIO.input(SensorDoPin):						
                print '    ****************'
		print '    * ! DANGER ! *'
		print '    ****************'
		print ''
				
		GPIO.output(LedPin, GPIO.LOW)	
		time.sleep(0.1)
		GPIO.output(LedPin, GPIO.HIGH)
			
	    else:
	        GPIO.output(LedPin, GPIO.LOW)
	    time.sleep(1)					

def destroy():
	GPIO.cleanup()				# Release resource

if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
