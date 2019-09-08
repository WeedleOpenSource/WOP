#!/usr/bin/env python
import ADC0832
import time
import RPi.GPIO as GPIO

LedPin = 16
thresholdVal = 150
def init():
	ADC0832.setup()
	GPIO.setup(LedPin, GPIO.OUT)

def loop():
	while True:
		analogVal = ADC0832.getResult(0)
		print 'analog value is %d' % analogVal
		if(analogVal < thresholdVal):
			GPIO.output(LedPin, GPIO.HIGH)
		else:
			GPIO.output(LedPin, GPIO.LOW)
                time.sleep(0.2)
			
if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'
