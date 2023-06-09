import RPi.GPIO as GPIO
from time import sleep
import time
import datetime
import dht11
   

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

###GPIO.setup(33,GPIO.IN)

GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)

instance=dht11.DHT11(pin=5)

while(True):
    result=instance.read()
    if result.is_valid():
        GPIO.output(18,False)
        print("Valid Input:- "+ str(datetime.datetime.now()))
        print("Temperature: %d  Celcius"%result.temperature)
        print("Humidity in IOT Lab:- %d %%" %result.humidity)
       
        if result.temperature>=29:
            GPIO.output(18,True)
           
    time.sleep(1)
