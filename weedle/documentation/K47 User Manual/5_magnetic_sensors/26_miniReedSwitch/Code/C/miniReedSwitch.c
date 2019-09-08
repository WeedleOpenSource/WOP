#include <wiringPi.h>
#include <stdio.h>

#define    reedPin    0
#define	   LedPin	  4

int cnt = 0;

int main(void)
{
	if(wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !\n");
		return -1; 
	}
	pinMode(LedPin, OUTPUT);
	pinMode(reedPin, INPUT);
	pullUpDnControl(reedPin, PUD_UP);
	while(1)
	{
		if(!digitalRead(reedPin))
		{
			printf("Magnet detected...\n");
			digitalWrite(LedPin, HIGH);
		}
		else
		{
			printf("No magnet detected...\n");
			digitalWrite(LedPin, LOW);
		}
		delay(200);
	}
	
	return 0;
}
