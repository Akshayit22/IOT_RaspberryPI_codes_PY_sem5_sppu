import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(36,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(37,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(33,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)

while True:
    GPIO.output(36,GPIO.HIGH) # LED ON
    sleep(1)
    GPIO.output(36,GPIO.LOW)  # LED OFF
    sleep(1)
    
    GPIO.output(37,GPIO.HIGH)
    sleep(1)
    GPIO.output(37,GPIO.LOW)
    sleep(1)
    
    GPIO.output(38,GPIO.HIGH)
    sleep(1)
    GPIO.output(38,GPIO.LOW)
    sleep(1)
    
    GPIO.output(33,GPIO.HIGH)
    sleep(1)
    GPIO.output(33,GPIO.LOW)
    sleep(1)