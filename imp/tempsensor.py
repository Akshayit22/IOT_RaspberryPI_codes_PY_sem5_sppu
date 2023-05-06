import RPi.GPIO as GPIO
import time
import datetime
import dht11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,False)


instance = dht11.DHT11(pin=5)

while True:
    result = instance.read()
    if result.is_valid():
        GPIO.output(3,False)
        print("Last valid input: "+ str(datetime.datetime.now()))
        print("Temperature: %d C" %result.temperature)
        print("Humidity:%d %%" %result.humidity)
        if result.humidity >=70:
            GPIO.output(3,True)



    time.sleep(1)
