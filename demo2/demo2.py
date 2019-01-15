#@Lauri Poikolainen 15.1.2019
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

#Ledit R=red, Y=yellow, G=green, jalankulkijoiden valojen eteen P
R=4
Y=17
G=27

PR=22
PG=5
PY=6
#B=button
B=16
PIR=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(Y, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(PR, GPIO.OUT)
GPIO.setup(PG, GPIO.OUT)
GPIO.setup(PY, GPIO.OUT)
GPIO.setup(B, GPIO.IN)
GPIO.setup(PIR, GPIO.IN)

while True:
	GPIO.output(G,1)
	GPIO.output(PR,1)
	if GPIO.input(B) == 1:
		odotus = time.time() + 15
                #Kohta 2.4, signaalivalo jalankulkijoille
		GPIO.output(PY,1)
                #Kohta 2.5, jos liikenne ei lopu, päästää jalankulkijat 15 sekunnin päästä menemään
                while time.time()<odotus:
			if GPIO.input(PIR)==0:
				break

                GPIO.output(Y,1)
		GPIO.output(G,0)
		time.sleep(3)
		GPIO.output(Y,0)
		GPIO.output(PY,0)
		GPIO.output(PR,0)
		GPIO.output(R,1)
		time.sleep(1)
		GPIO.output(PG,1)
		time.sleep(6)
		GPIO.output(R,0)
		GPIO.output(PG,0)
		GPIO.output(Y,1)
		GPIO.output(PR,1)
		time.sleep(2)
		GPIO.output(Y,0)
		
GPIO.cleanup()
