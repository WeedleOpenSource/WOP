K47 Modules Sensor Kit for Raspberry Pi

Kuman Trading Shenzen Company, Ltd.
Support, FAQ, and more info: http://www.kumantech.com

Last Revision Date: 12 June 2018

1. Introduction

Congratulations on acquiring the K47 sensor kit! Using these tools you'll be able to embed your Raspberry Pi in the real world by detecting (and in many cases, producing) sound, light, motion, temperature, and other physical phenomena. These sensors vastly expand the input and output possibilities of your Raspberry Pi, and will provide many hours of exploration and enjoyment. 

This documentation package assumes you own a Raspberry Pi, have installed its OS, and have basic familiarity with its use. If you are new to Raspberry Pi a good starting point is https://www.raspberrypi.org/help/.

2. About This Documentation

This package consists of this Read Me file, which introduces you to Raspberry development using the K47 sensors, and then subfolders describing the many sensors in your kit. These sensor folders contain a variety of information, including wiring diagrams in JPG, sample code in C and Python, and most importantly, a written Description (.docx/.pdf) introducing you to the physics of the sensor and how to interface it to your Raspberry Pi.

If you are new to working with sensors or interfacing your Raspberry Pi to external hardware components, please see the "Introduction To Sensors" document for help getting started. Even if you are an experienced Raspberry Pi designer, you might briefly consult this document for a quick introduction to all the sensors in this kit. If you have never used a solderless breadboard before, please also see the document titled "How To Use A Breadboard."

3. About Analog Sensing with the ADC0832

The GPIO pins on your Raspberry Pi are purely digital -- they are either "on" or "off." By contrast, physical phenomena are often analog, which is to say continuous in nature or varying over some spectrum. In order to use sensors that measure analog phenomena, you will also use the ADC0832 Analog/Digital Converter (ADC) included with this kit to translate the analog responses of the sensor into digital responses usable on the Raspberry Pi. 

Consult an individual sensor's description (in its documentation subfolder) to see if that sensor requires ADC, and if so, how to connect it between the sensor and your Raspberry Pi. For your reference, a datasheet for the ADC0832 is included but you will not need this to successfully use the ADC0832 with K47 sensors.

4. Development Software Installation

To conveniently access the GPIO pins on your Raspberry Pi, most Raspberry Pi programs---and K47's sample code----use the open source WiringPi library (http://wiringpi.com).  You will need to install this library, and the Python interpreter, on your Raspberry Pi before compiling these programs. Follow these steps (and issue these commands) when your Raspberry Pi is connected to the internet:

	a. Install Python Interpreter and GPIO library
	
		sudo apt-get install python-dev
		sudo apt-get install python-pip
		sudo pip install rpi.gpio
		
	b. Install Git (to access the most recent WiringPi library)
	
		sudo apt-get install git-core
	
	c. Create a local folder for the WiringPi library, download it, and build it
	
		mkdir lib_wiringPi
		cd lib_wiringPi
		git clone git://git.drogon.net/wiringPi
		cd wiringPi
		./build
		
A successful installation will be confirmed by the following notice:  "All Done. NOTE: To compile programs with wiringPi, you need to add: -lwiringPi to your compile line(s). To use the Gertboard, MaxDetect, etc. code (the devLib), you need to also add: -lwiringPiDev to your compile lines." This notice applies only to C source code. See the next note "About Source Code Dependencies."

5. About Source Code Dependencies

Certain source code files can refer to other files and libraries existing elsewhere on your system. To compile these files successfully, you must alert the compiler to these external dependencies:

	a. To compile any C program that #includes "wiringPi.h" header, add "-lwiringPi" to your gcc command line.
	
		e.g.:	gcc led.c -o led.out -lwiringPi -lm
	
		Note the library name is case-sensitive ("P" is capitalized).
	
	b. To compile any C program that #includes "math.h", add "-lm" to your gcc command line.
	
6. Support

We recognize that our sample code and sensor documentation may not fit the needs of all users. If you have questions, please don't hesitate to contact Customer Service. We are happy to help and wish you the best success with your new tools!

