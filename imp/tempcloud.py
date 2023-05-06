import RPi.GPIO as GPIO     #it contains config for all pins 
import time                 #for sleep
import dht11                #dht11 senor so include those package
import datetime
import httplib , urllib
key = '3510LHO9JHCWWPYT'
#initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)     #for alarm

#read data using pin 14
instance=dht11.DHT11(pin=5) #for reading

while True:
	t=dht11.read_retry(1,3)
	print "temperature",t

	parameters=urllib.urlencode('field1':t,'key':key)

	headers={"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}

	con=httplib.HTTPConnection("api.thingspeak.com:80")

	con.request("POST","/update",parameters,headers)

	response=conn.getrespose()

	print (response.status,"\t",reponse.reason)
	data=response.read()
	conn.close()
	time.sleep(1) 
