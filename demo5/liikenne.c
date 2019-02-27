#include <stdio.h>
#include <wiringPi.h>

#define RED 18
#define YELLOW 23
#define GREEN 24
#define PRED 17
#define PGREEN 27
#define BUTTON 22

int main() {
	//Valmistetaan pinnit ottamaan vastaan 
	wiringPiSetupGpio();
	pinMode(RED,OUTPUT);
	pinMode(YELLOW, OUTPUT);
	pinMode(GREEN, OUTPUT);
	pinMode(PRED, OUTPUT);
	pinMode(PGREEN,OUTPUT);
	pinMode(BUTTON,INPUT);
	//pyörii jatkuvasti, ei pääse kohtaan return 0
	while(1){	
		digitalWrite(GREEN,HIGH);
		digitalWrite(PRED, HIGH);
		//kuuntelee nappulaa
		if(digitalRead(BUTTON)){
			delay(3000);
			digitalWrite(GREEN,LOW);
			digitalWrite(YELLOW,HIGH);
			delay(4000);
			digitalWrite(YELLOW, LOW);
			digitalWrite(RED,HIGH);
			delay(2000);
			digitalWrite(PRED, LOW);
			digitalWrite(PGREEN,HIGH);
			delay(8000);
			digitalWrite(PGREEN,0);
			digitalWrite(PRED, HIGH);
			digitalWrite(YELLOW, HIGH);
			digitalWrite(RED,LOW);
			delay(2000);
			digitalWrite(YELLOW,LOW);
			digitalWrite(GREEN, HIGH);
		}
	}
	return 0;
}
