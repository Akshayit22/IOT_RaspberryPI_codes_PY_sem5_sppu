
import RPi.GPIO as GPIO
from time import sleep 
 


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(38,GPIO.OUT , initial = GPIO.LOW)

while True:
    
    GPIO.output(38,GPIO.HIGH)
    sleep(2)
    GPIO.output(38,GPIO.LOW)            
    sleep(1)

    
