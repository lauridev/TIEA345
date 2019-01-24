#@author Lauri Poikolainen 21.1.2019
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
from picamera import PiCamera

camera = PiCamera()
pin=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)

while True:
    if GPIO.input(pin)==1:
        camera.capture("/var/www/html/kuvat/viimeisin.jpg")
