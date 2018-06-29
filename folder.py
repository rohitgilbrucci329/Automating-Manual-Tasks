#install the package first
#pip3 install python3-xlib
#pip3 install pyautogui

import pyautogui, time
import os, errno
import os.path
import pathlib

x=1;
y=1;
j=1;
onlyfiles = next(os.walk(r'D:\Project Files\DCM FILE'))[2] #dir is your directory path as string
y=len(onlyfiles)

file_list = os.listdir('D:\Project Files\DCM FILE')

print(file_list)


for i in range(1,y):
	
	try:
	    os.makedirs('D:\Dicom images\%s' %file_list[i-1])
	except OSError as e:
	    if e.errno != errno.EEXIST:
	        raise    

