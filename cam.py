

import time 
import os 
import sys
os.system('clear')

while True:
	print("Do you want to click a Picture?")

	print('1.yes')
	
	print('2.No')
	
	choice=input('Enter yours choice:')
	if choice=='1':
		os.system('fswebcam /home/pi/Desktop/A1/img123.jpg')
			
			
	elif choice=='2':
			
		print('OK')
		break
		
	
