import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

while True:
	GPIO.output(10,GPIO.HIGH)
	GPIO.output(11,GPIO.HIGH)
	sleep(1)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(11,GPIO.LOW)
	sleep(1)
