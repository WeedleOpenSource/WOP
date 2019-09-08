#include <wiringPi.h>
#include <stdio.h>

#define ShockPin      0
#define LedPin        4

void myISR(void)
{
	printf("shock occured.\n");
	if(digitalRead(LedPin) == HIGH)
	{
		digitalWrite(LedPin, LOW);	
	}
    else
	{
		digitalWrite(LedPin, HIGH);
	}		
}


int main(void)
{
	if(wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !\n");
		return 1; 
	}
	
	pinMode(ShockPin,  INPUT);
	pinMode(LedPin,   OUTPUT);

	if(wiringPiISR(ShockPin, INT_EDGE_FALLING, &myISR) == -1)
	{
		printf("setup ISR failed !");
		return 1;
	}
	while(1);

	return 0;
}
