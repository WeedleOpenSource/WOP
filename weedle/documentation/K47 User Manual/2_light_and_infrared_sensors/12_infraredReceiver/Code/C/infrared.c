#include <wiringPi.h>
#include <stdio.h>

#define    IrEmissionPin    0
#define	   IrReceiverPin	16
#define	   LEDPin	4

int cnt = 0;

void infraredDetectionInterruptHandler(void)
// called at interrupt every time the IR receiver pin's signal falls to LOW

{
	printf("Received infrared signal. cnt = %d\n", ++cnt);
    
    // blink the LED briefly
	if(digitalRead(LEDPin) == HIGH)
	{
		digitalWrite(LEDPin, LOW);
	}
    else
	{
		digitalWrite(LEDPin, HIGH);
	}
    
	delay(100);
	digitalWrite(LEDPin, LOW);
}

int main(void)
{
	if(wiringPiSetup() == -1)
	{ 
		printf("setup wiringPi failed !\n");
		return -1; 
	}
	pinMode(LEDPin, OUTPUT);
	pinMode(IrEmissionPin, OUTPUT);
	pinMode(IrReceiverPin, INPUT);
	pullUpDnControl(IrReceiverPin, PUD_UP) 
	
    // register an interrupt service routine that will
    // be called every time the IR receiver pin goes LOW
    
	if(wiringPiISR(IrReceiverPin, INT_EDGE_FALLING, &infraredDetectionInterruptHandler) == -1)
	{
		printf("setup ISR failed !");
		return -1;
	}
    
    // now loop forever, from time to time blinking the IR
    // emitter ON and OFF.  If the receiver receives the emitter's emission,
    // then the interrupt routine should report to us "I saw it!" shortly after
    // this emitter logic tells us "I sent it!"
    
	while(1)
	{
		digitalWrite(IrEmissionPin, HIGH);
		printf("IrEmissionPin is set High\n");
		delay(500);
		
		digitalWrite(IrEmissionPin, LOW);
		printf("IrEmissionPin is set Low\n");
		delay(500);
	}
	
	return 0;
}
