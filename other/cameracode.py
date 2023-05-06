

import os
import sys
import time

#os.system('clear')
i=0
while True:
	i+=1
	print('Do you want to click a picture? ')
	print('1. Yes')
	print('2. No')
	choice = input('Enter your choice: ')
	if choice == '1':
		img_name='img_'+str(i)
		string='fswebcam /home/pi/Desktop/capturedImages/'+img_name+'.jpg'
		print(string)
		#os.system('fswebcam /home/pi/Desktop/capturedImages/xyz.jpg')
		# os.system('fswebcam C:/Users/Akshay L Telang/Documents/assign_sem5/iot')
	elif choice == '2':
		print('Ok!')
		break
	else:
		print('Invalid choice')
	
	
