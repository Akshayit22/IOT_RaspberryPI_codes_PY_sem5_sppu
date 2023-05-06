import RPi.GPIO as GPIO
import time
import os

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
			os.system('fswebcam -r 320x240 --jpeg 50 --save /home/pi/Desktop/Iot/webcamImage/%H%M%S.jpg') 
			GPIO.output(37,GPIO.HIGH)
