import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pinno = 38
BUZZER = 32
ledno = 37
GPIO.setup(pinno,GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(ledno, GPIO.OUT)
flag = True
while True:
    if (GPIO.input(pinno)!=0 and flag):
        print("yes")
        GPIO.output(BUZZER, True)
        GPIO.output(ledno, True)
        sleep(0.3)
        flag = False
    else:
        GPIO.output(BUZZER, False)
        GPIO.output(ledno, False)
        flag = True
    
