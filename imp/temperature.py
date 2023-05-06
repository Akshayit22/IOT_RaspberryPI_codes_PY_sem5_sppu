import RPi.GPIO as GPIO
import dht11
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

instance = dht11.DHT11(pin=33)

for i in range (0,5):
    result=instance.read()
    if (result.is_valid()):
        print(f"Temperature: {result.temperature}")
        print(f"Humidity: {result.humidity}")
    else:
        print(f"Error: {result.error_code}")
    sleep(5);

