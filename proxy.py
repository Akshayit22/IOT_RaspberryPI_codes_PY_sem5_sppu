import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(33,GPIO.IN)
GPIO.setup(36,GPIO.OUT, initial=GPIO.LOW)

while (True):
    i=GPIO.input(33)
    sleep(1)
    if(i == 0):
        print('No Obstacle')
        GPIO.output(36,GPIO.LOW)
    else:
        print('Obstacle')
        GPIO.output(36,GPIO.HIGH)
