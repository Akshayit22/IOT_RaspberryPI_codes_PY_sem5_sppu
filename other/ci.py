import os
import sys
import time

os.system('clear')
i=0
strr='a'

while True:
	i+=1
    print('Do you want to click a picture?')
	print('1. Yes')
	print('2. No')
	choice = input('Enter your choice: ')
	print()
	if choice == '1':
		string = 'fswebcam /home/pi/Desktop/capturedImages/p'+i*strr+'.jpg'
		#os.system('fswebcam /home/pi/Desktop/capturedImages/p2.jpg')
		print(string)
	elif choice == '2':
		typewriter('Ok!')
		break
	else:
		typewriter('Invalid choice')
	
	

