
import time
import RPi. GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)

trig = 33      # GPIO pin numbers
echo = 12

GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)

while True:
    GPIO.output(trig,True)
    time.sleep(0.00001) # 10 microseconds
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        print("Not Obstacle")
    
    start = time.time()
    
    while GPIO.input(echo) == 1:
        print("Obstacle")
    
    end = time.time()
    
    distance = ((end - start) * 34300) / 2
    print ("distance:", distance, "cm")
    time.sleep(0.5)
