import RPi.GPIO as GPIO
from time import sleep 
import datetime
import dht11
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


GPIO.setup(33,GPIO.IN)
GPIO.setup(18,GPIO.OUT,INITIAL=GPIO.LOW)

instance = dht11.DHT11(pin=5)

while(True):
	
	Results= instance.read()
	if Results.is_valid():
		GPIO.output(18,False)
		print('Last valid Input '+ str(datetime.datetime.now()))
		print('Temprature is %d C ' %Results.temperature)
		print('Humidity %d '%Results.humidity)
		
		if Results.temperature>=29:
			GPIO.output(18,True)
		
	time.sleep(1)
