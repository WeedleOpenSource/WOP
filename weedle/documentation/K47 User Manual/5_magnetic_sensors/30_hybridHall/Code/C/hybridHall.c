#include <wiringPi.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

#define     ADC_CS    0
#define     ADC_CLK   1
#define     ADC_DIO   2

#define  Hall_DO_Pin   3
#define  LedPin		   4
#define thresholdVal	100

typedef unsigned char uchar;
typedef unsigned int uint;


uchar get_ADC_Result(void)
{
	uchar i;
	uchar dat1=0, dat2=0;

	digitalWrite(ADC_CS, 0);
	digitalWrite(ADC_CLK,0);
	digitalWrite(ADC_DIO,1);	delayMicroseconds(2);
	digitalWrite(ADC_CLK,1);	delayMicroseconds(2);

	digitalWrite(ADC_CLK,0);	
	digitalWrite(ADC_DIO,1);    delayMicroseconds(2);
	digitalWrite(ADC_CLK,1);	delayMicroseconds(2);

	digitalWrite(ADC_CLK,0);	
	digitalWrite(ADC_DIO,0);	delayMicroseconds(2);
	digitalWrite(ADC_CLK,1);	
	digitalWrite(ADC_DIO,1);    delayMicroseconds(2);
	digitalWrite(ADC_CLK,0);	
	digitalWrite(ADC_DIO,1);    delayMicroseconds(2);
	
	for(i=0;i<8;i++)
	{
		digitalWrite(ADC_CLK,1);	delayMicroseconds(2);
		digitalWrite(ADC_CLK,0);    delayMicroseconds(2);

		pinMode(ADC_DIO, INPUT);
		dat1=dat1<<1 | digitalRead(ADC_DIO);
	}
	
	for(i=0;i<8;i++)
	{
		dat2 = dat2 | ((uchar)(digitalRead(ADC_DIO))<<i);
		digitalWrite(ADC_CLK,1); 	delayMicroseconds(2);
		digitalWrite(ADC_CLK,0);    delayMicroseconds(2);
	}

	digitalWrite(ADC_CS,1);
	pinMode(ADC_DIO, OUTPUT);
	return(dat1==dat2) ? dat1 : 0;
}

int main(void)
{
	uchar digitalVal = 1;
	uchar analogVal = 0;
	if(wiringPiSetup() == -1)
	{
		printf("setup wiringPi failed !\n");
		return -1; 
	}
    

	pinMode(ADC_CS,  OUTPUT);
	pinMode(ADC_CLK, OUTPUT);
	pinMode(Hall_DO_Pin, INPUT);
	pullUpDnControl(Hall_DO_Pin, PUD_UP);
	pinMode(LedPin, OUTPUT);

	while(1)
	{
		if((digitalVal = digitalRead(Hall_DO_Pin)))
		{
			printf("Do is %d.\n", digitalVal);
			analogVal = get_ADC_Result();
			printf("Current analog value is %d.\n", analogVal);
			if(analogVal > thresholdVal)
			{
				digitalWrite(LedPin, HIGH);
			}
			delay(200);
		}
		else
		{
			digitalWrite(LedPin, LOW);
		}
	}

	return 0;
}

