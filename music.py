import RPi.GPIO as GPIO
from time import sleep

BUZZER = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.HIGH)
GPIO.output(BUZZER, GPIO.LOW)

def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
       GPIO.output(BUZZER, True)
       sleep(halveWaveTime)
       GPIO.output(BUZZER, False)
       sleep(halveWaveTime)
def play():
    t=0
    notes=[262,294,330,262,262,294,330,262,330,349,392,330,349,392,392,440,392,349,330,262,392,440,392,349,330,262,262,196,262,262,196,262]
    duration=[5]
    for n in notes:
        buzz(n, duration[t])
        sleep(duration[t] *0.1)

play()


