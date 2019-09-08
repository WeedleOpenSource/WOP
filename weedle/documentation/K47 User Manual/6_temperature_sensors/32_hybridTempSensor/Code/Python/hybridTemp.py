#!/usr/bin/env python
import RPi.GPIO as GPIO
import ADC0832
import time

TempSensor_DO_PIN = 15

def init():
	GPIO.setmode(GPIO.BOARD)	
	GPIO.setup(TempSensor_DO_PIN, GPIO.IN)
	ADC0832.setup()
def loop():	
    while True:
        global digitalVal
        print 'Current analog value is %d'%  ADC0832.getResult(0)
        digitalVal = GPIO.input(TempSensor_DO_PIN)
        if(digitalVal == 1):
            print "Temperature alarm ... threshold exceeded!"
        else:
        	pass
        	
	    time.sleep(0.2)
        
if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'
