import RPi.GPIO as GPIO
import time

TRIG=24               
ECHO=26

GPIO.setmode(GPIO.BOARD)

while True:
    print('distance measurement in progress')
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(33, GPIO.OUT)

    GPIO.output(TRIG,False)
    print('waiting for sensor to settle')
    time.sleep(0.2)

    GPIO.output(TRIG,True)
    time.sleep(0.0001)

    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()

    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print('distance: ',distance,' in cm')
    if distance <=10:
        GPIO.output(33, True)
    else:
        GPIO.output(33, False)
        
    time.sleep(2)    