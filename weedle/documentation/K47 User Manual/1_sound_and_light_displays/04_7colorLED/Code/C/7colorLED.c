#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>

typedef unsigned char uchar;

#define LedPin    16

int main(void)
{
	int i;

	if(wiringPiSetup() == -1)
	{ 
		printf("setup wiringPi failed !");
		return -1; 
	}
	
	pinMode(LedPin, OUTPUT);
	while(1)
	{
		digitalWrite(LedPin, HIGH);   	
	}

	return 0;
}
