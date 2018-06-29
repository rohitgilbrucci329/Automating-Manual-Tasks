
#install the package first
#pip3 install python3-xlib
#pip3 install pyautogui

import pyautogui, time
import os
import os.path
import pathlib



def openFile():
	
		os.startfile('C:\Program Files\RadiAntViewer64bit\RadiAntViewer.exe')


openFile();

file_list = os.listdir('D:\Project Files\DCM FILE') #to get the list of files in the directory

x=1;
y=1;
j=1;
onlyfiles = next(os.walk('D:\Project Files\DCM FILE'))[2] #dir is your directory path as string
y=len(onlyfiles)
s=190779750

time.sleep(3)

for i in range(1,y):

	try:
		loc=pyautogui.locateOnScreen('radiant1.png'); c=pyautogui.center(loc)
		pyautogui.click((c))

	except:
		loc=pyautogui.locateOnScreen('radiant2.png'); c=pyautogui.center(loc)
		pyautogui.click((c))

	time.sleep(3)


	pyautogui.keyDown('ctrl'); pyautogui.press('o'); pyautogui.keyUp('ctrl')

	time.sleep(10)

	pyautogui.typewrite('%s' %file_list[i-1]); time.sleep(2); pyautogui.press('enter')
	time.sleep(10)

	size=os.path.getsize('D:\Project Files\DCM FILE\%s' %file_list[i-1])

	time.sleep(20+150*size/s)

	pyautogui.keyDown('ctrl'); pyautogui.press('e'); pyautogui.keyUp('ctrl')

	time.sleep(3)

	try:
		loc2=pyautogui.locateOnScreen('series.png'); c2=pyautogui.center(loc2)
		pyautogui.click((c2)); 
	except:
		print("\n")

	time.sleep(3)

	try:
		loc3=pyautogui.locateOnScreen('export1.png'); c3=pyautogui.center(loc3)
		pyautogui.click((c3)); 

	except: 
		loc3=pyautogui.locateOnScreen('export2.png'); c3=pyautogui.center(loc3)
		pyautogui.click((c3)); 


	time.sleep(3)

	pyautogui.typewrite('f') #to write
	time.sleep(3)

	pyautogui.typewrite('D:\Dicom images\%s' %file_list[i-1]); 
	time.sleep(3)
	pyautogui.press('enter');

	time.sleep(3)

	pyautogui.press('enter')

	time.sleep(20+110*size/s)















