import  RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(33,GPIO.IN)
GPIO.setup(37,GPIO.OUT)

while(True):
		i= GPIO.input(33)
		if(i==0):
			print('Not Detected!')
			GPIO.output(37,GPIO.LOW)
		else:
			print('Obstacle')
			GPIO.output(37,GPIO.HIGH)
