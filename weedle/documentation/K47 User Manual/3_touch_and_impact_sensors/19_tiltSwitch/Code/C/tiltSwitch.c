#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <wiringPi.h>

#define  TiltPin     0
#define   LedPin     4

int main(void)
{
	if(wiringPiSetup() < 0)
	{
		printf( " setup wiringPi failed!\n");
		return -1;
	}

	pinMode(TiltPin, INPUT);
	pinMode(LedPin, OUTPUT);

	while(1)
	{
		if(0 == digitalRead(TiltPin))
		{
			digitalWrite(LedPin, HIGH);	
		}	
		else
		{
			digitalWrite(LedPin, LOW);	
		}
	}

	return 0;
}
