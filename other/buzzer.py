import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
                                                                                                                                                           
n1=int(input('Enter the pin 1:'))
n2=int(input('Enter the pin 2:'))
n3=int(input('Enter the pin 3:'))
n4=int(input('Enter the pin 4:'))
n=int(input('Enter count: '))


GPIO.setup(36,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(5,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(33,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(22,GPIO.OUT,initial=GPIO.LOW)

for i in range (n):
    GPIO.output(n1,GPIO.HIGH)
    sleep(1)
    GPIO.output(22,GPIO.HIGH)
    sleep(1)
    GPIO.output(n1,GPIO.LOW)
    sleep(1)
    GPIO.output(22,GPIO.LOW)
    sleep(1)
    
    GPIO.output(n2,GPIO.HIGH)
    sleep(1)
    GPIO.output(22,GPIO.HIGH)
    sleep(1)
    GPIO.output(n2,GPIO.LOW)
    sleep(1)
    GPIO.output(22,GPIO.LOW)
    sleep(1)
    
    GPIO.output(n3,GPIO.HIGH)
    sleep(1)
    GPIO.output(22,GPIO.HIGH)
    sleep(1)
    GPIO.output(n3,GPIO.LOW)
    sleep(1)
    GPIO.output(22,GPIO.LOW)
    sleep(1)
    
    
    GPIO.output(n4,GPIO.HIGH)
    sleep(1)
    GPIO.output(22,GPIO.HIGH)
    sleep(1)
    GPIO.output(n4,GPIO.LOW)
    sleep(1)
    GPIO.output(22,GPIO.LOW)
    sleep(1)
    
    
    
    