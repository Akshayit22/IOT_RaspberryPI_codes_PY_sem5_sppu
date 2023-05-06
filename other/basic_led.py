import RPi.GPIO as GPIO
from time import sleep

from datetime import datetime
import smtplib

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(38, GPIO.IN)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)


def send_mail(from_mail, to_mail):
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    content= "Mail sent from NAS041 for obstacle detected"
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    sender= from_mail
    recipient= to_mail
    mail.login('samplemail992@gmail.com','wqbnyihafvfkeosv')
    header='To:'+recipient+'\n'+'From:'\
    +sender+'\n'+'subject:testmail\n'
    content=header+content
    mail.sendmail(sender,recipient, content)
    print('Sent')
    mail.close()


while True: 
    i = GPIO.input(38)
    if (i == 1):
        print('Obstacle')
        send_mail('samplemail992@gmail.com', 'ipriyadarshini@kkwagh.edu.in')
        GPIO.output(22, GPIO.HIGH)
        sleep(1)
        GPIO.output(22, GPIO.LOW)
        break
    else:
        GPIO.output(22, GPIO.LOW)
        print('No Obstacle')
        