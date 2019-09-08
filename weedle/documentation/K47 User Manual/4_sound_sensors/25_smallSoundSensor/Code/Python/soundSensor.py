#!/usr/bin/env python
import RPi.GPIO as GPIO
import ADC0832
import time

Sound_DO_PIN = 15

def init():
	GPIO.setmode(GPIO.BOARD)	
	GPIO.setup(Sound_DO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	ADC0832.setup()
	
def loop():	
    while True:
        global digitalVal
        digitalVal = GPIO.input(Sound_DO_PIN)
        if(digitalVal == 0):
            print 'DO is %d' % digitalVal
            print "voice in..."
	    print 'Current analog value is %d'%  ADC0832.getResult(0)
        else:
            pass

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'
