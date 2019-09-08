#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

IrReceiverPin = 10
IrEmissionPin = 11
LedPin = 16

Led_status = 1

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(IrReceiverPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(IrEmissionPin, GPIO.OUT)   # Set IrPin's mode is output
	GPIO.output(LedPin, GPIO.LOW) # Set LedPin low to off led

def irReceivedCallback(ev=None): # Called every time the irReceiver pin falls. Blink the LED!
	global Led_status
	Led_status = not Led_status
	GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
	print("received signal!\n")
	time.sleep(0.1)
	GPIO.output(LedPin, False)

def loop():
	GPIO.add_event_detect(IrReceiverPin, GPIO.FALLING, callback=irReceivedCallback) # wait for falling
	while True:
		print '...IrPin high'
		GPIO.output(IrEmissionPin, GPIO.HIGH)  # IrPin on
		time.sleep(0.5)
		print 'IrPin low...'
		GPIO.output(IrEmissionPin, GPIO.LOW) # IrPin off
		time.sleep(0.5)

def destroy():
	GPIO.output(LedPin, GPIO.LOW)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                print("KeyboardInterrupt.\n")
		destroy()

