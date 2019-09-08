#include <wiringPi.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>



#define  Reed_AO_Pin   0
#define  LedPin		   4


typedef unsigned char uchar;
typedef unsigned int uint;



int main(void)
{
	uchar digitalVal = 1;
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}
    
	pinMode(Reed_AO_Pin, INPUT);
	pinMode(LedPin, OUTPUT);

	while(1){
		if((digitalVal = digitalRead(Reed_AO_Pin)) == 0)
		{
			printf("Magnet detected!\n");
			digitalWrite(LedPin, HIGH);
			delay(200);
		}
		else
		{
			digitalWrite(LedPin, LOW);
		}
	}

	return 0;
}

