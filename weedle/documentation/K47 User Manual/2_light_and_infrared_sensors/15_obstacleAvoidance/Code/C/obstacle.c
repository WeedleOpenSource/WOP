#include <wiringPi.h>
#include <stdio.h>

#define ObstaclePin 0
#define LedPin		4

int main(void)
{
	if(wiringPiSetup() == -1)
	{ 
		printf("setup wiringPi failed !\n");
		return -1; 
	}
	
	pinMode(LedPin, OUTPUT);
	while(1)
	{
		if(0 == digitalRead(ObstaclePin))
		{
			printf("Barrier detected!\n");
			digitalWrite(LedPin, HIGH);
		}
		else
		{
			digitalWrite(LedPin, LOW);
		}
	}
	return 0;
}
