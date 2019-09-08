#!/usr/bin/env python
import RPi.GPIO as GPIO
import ADC0832
import time

Touch_DO_PIN = 15

def init():
	GPIO.setmode(GPIO.BOARD)	
	GPIO.setup(Touch_DO_PIN, GPIO.IN, pull_up_down = PUD_DOWN)
	ADC0832.setup()
def loop():
    print 'Please touch....\n'
    while True:
        global digitalVal
		print 'Current analog value is %d'%  ADC0832.getResult(0)
		
        digitalVal = GPIO.input(Touch_DO_PIN)
        if(digitalVal == 1):
            print 'DO is %d' % digitalVal
            print "Touch detected..."
            time.sleep(0.2)
        else:
            pass

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print "The end !"
