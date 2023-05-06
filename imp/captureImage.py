import os
import sys
import time

os.system('clear')

def typewriter(msg):
	for char in msg:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)

while True:
	typewriter('Do you want to click a picture? ')
	print()
	typewriter('1. Yes')
	print()
	typewriter('2. No')
	print()
	choice = input('Enter your choice: ')
	print()
	if choice == '1':
		os.system('fswebcam /home/pi/Desktop/capturedImages/p2.jpg')
	elif choice == '2':
		typewriter('Ok!')
		break
	else:
		typewriter('Invalid choice')
	
	
