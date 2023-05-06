#Libraries
import RPi.GPIO as GPIO
import time
import vlc

p1 = vlc.MediaPlayer("/home/pi/piano/68437__pinkyfinger__piano-a.wav")
p2 = vlc.MediaPlayer("/home/pi/piano/68438__pinkyfinger__piano-b.wav")
p3 = vlc.MediaPlayer("/home/pi/piano/68439__pinkyfinger__piano-bb.wav")
p4 = vlc.MediaPlayer("/home/pi/piano/68440__pinkyfinger__piano-c.wav")
p5 = vlc.MediaPlayer("/home/pi/piano/68441__pinkyfinger__piano-c.wav")
p6 = vlc.MediaPlayer("/home/pi/piano/68442__pinkyfinger__piano-d.wav")
p7 = vlc.MediaPlayer("/home/pi/piano/68443__pinkyfinger__piano-e.wav")
p8 = vlc.MediaPlayer("/home/pi/piano/68444__pinkyfinger__piano-eb.wav")


 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
#set GPIO Pins
PIN_TRIGGER = 15
PIN_TRIGGER3 = 32
PIN_TRIGGER2 = 26
PIN_TRIGGER1 = 3
GPIO_ECHO = 16
GPIO_ECHO1 = 13
GPIO_ECHO2 = 11
GPIO_ECHO3 = 5
 
#set GPIO direction (IN / OUT)
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
GPIO.setup(PIN_TRIGGER3, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(GPIO_ECHO3, GPIO.IN)
 
def distance(ECHO_PIN, TRIGGER_PIN):
    
    # set Trigger to HIGH
    GPIO.output(TRIGGER_PIN, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, False)
 
    StartTime = time.time()
    StopTime = time.time()
    
    time_limit = time.time()
 
    # save StartTime
    while GPIO.input(ECHO_PIN) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(ECHO_PIN) == 1:
        StopTime = time.time()
        if (time.time() - time_limit) > 0.004:
            return -1
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist1 = distance(16,15)
            dist2 = distance(13,3)
            dist3 = distance(11,26)
            dist4 = distance(5,32)
            print ("%.1f cm \t %.1f cm \t %.1f cm \t %.1f cm" % (dist1, dist2, dist3 ,dist4))
            
            if dist1 < 30 and dist1 > -1:
                p2.stop()
                p3.stop()
                p4.stop()
                p5.stop()
                p6.stop()
                p7.stop()
                p8.stop()
                p1.play()
            elif dist1 > 30:
                p1.stop()
                p3.stop()
                p4.stop()
                p5.stop()
                p6.stop()
                p7.stop()
                p8.stop()
                p2.play()
            elif dist2 < 30 and dist2 > -1:
                p1.stop()
                p2.stop()
                p4.stop()
                p5.stop()
                p6.stop()
                p7.stop()
                p8.stop()
                p3.play()
            elif dist2 > 30:
                p1.stop()
                p2.stop()
                p3.stop()
                p5.stop()
                p6.stop()
                p7.stop()
                p8.stop()
                p4.play()
            elif dist3 < 30 and dist3 > -1:
                p1.stop()
                p2.stop()
                p3.stop()
                p4.stop()
                p7.stop()
                p8.stop()
                p6.stop()
                p5.play()
            elif dist3 > 30:
                p1.stop()
                p2.stop()
                p3.stop()
                p5.stop()
                p4.stop()
                p7.stop()
                p8.stop()
                p6.play()
            elif dist4 < 30 and dist4 > -1:
                p1.stop()
                p2.stop()
                p3.stop()
                p5.stop()
                p6.stop()
                p4.stop()
                p8.stop()
                p7.play()
            elif dist4 > 30:
                p1.stop()
                p2.stop()
                p3.stop()
                p5.stop()
                p6.stop()
                p7.stop()
                p4.stop()
                p8.play()
            else:
                p1.stop()
                p2.stop()
                p3.stop()
                p4.stop()
                p5.stop()
                p6.stop()
                p7.stop()
                p8.stop()
                
            print("Dist1 : " + str(dist1) + " Dist2 = " + str(dist2) + " Dist3 = " + str(dist3) + " Dist4 = " + str(dist4))
            print("dist_1  : " + str(dist1) + "dist_2 : " + str(dist2))
            time.sleep(0.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
