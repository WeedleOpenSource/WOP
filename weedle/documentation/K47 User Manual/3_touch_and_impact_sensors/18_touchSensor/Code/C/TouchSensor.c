#include <wiringPi.h>
#include <stdio.h>

#define TouchPin    0
#define LedPin      4

int main(void)
{
	if(wiringPiSetup() == -1)
	{ 
		printf("setup wiringPi failed !");
		return -1; 
	}
	
	pinMode(TouchPin, INPUT);
	pinMode(LedPin,  OUTPUT);

	while(1)
	{
		digitalWrite(LedPin, digitalRead(TouchPin));
		delay(200);
	}

	return 0;
}
