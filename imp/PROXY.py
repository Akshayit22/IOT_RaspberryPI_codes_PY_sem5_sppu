import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(33,GPIO.IN)

GPIO.setup(12,GPIO.OUT,initial=GPIO.LOW)



while (True):
    i=GPIO.input(33)
    if(i == 0):
        print('No Obstacle')
        GPIO.output(12,GPIO.LOW)
    else:
        print('Obstacle')
        GPIO.output(12,GPIO.HIGH)
     
    