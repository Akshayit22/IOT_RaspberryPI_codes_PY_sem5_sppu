# import libraries


import time 
import os 

while True: # do forever

	ans=int(input("Do you want to take a picture(1/0): "))

	if ans==1:
		os.system('fswebcam  /home/pi/Desktop/Iot/webcamImage/ABC.jpg') 
	else:
		exit()
