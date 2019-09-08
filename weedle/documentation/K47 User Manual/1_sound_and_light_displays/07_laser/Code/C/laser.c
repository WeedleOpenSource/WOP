#include <wiringPi.h>
#include <stdio.h>

#define LaserPin    0
#define	LedPin		4

int main(void)
{
	if(wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !");
		return -1; 
	}

	pinMode(LaserPin, OUTPUT);
	pinMode(LedPin, OUTPUT);
	while(1)
	{
		digitalWrite(LaserPin, HIGH);
		digitalWrite(LedPin, HIGH);
		printf("Laser on....\n");
		delay(1000);
		
		digitalWrite(LaserPin, LOW);
		digitalWrite(LedPin, LOW);
		printf("Laser off....\n");
		delay(1000);
	}

	return 0;
}
