# Automating-Manual-Tasks

# Instructions for automating:

1) Keep all the files downloaded from this repository on desktop.
2) Directory in which medical images should be there is D:\Project Files\DCM FILE. (Make a directory Project Files and inside which another called DCM FILE)
3) If the directory is to be changed or to be kept the default directory i.e. the one which had been used by radiant the very last time 
 (the one which shows up first when you click ctrl + O), replace its address with "D:\Project Files\DCM FILE" in the code everywhere since my default directory of operation was 
D:\Project Files\DCM FILE where all the dicom files were stored.
4) If the code is to remain the same, make sure that this is the directory of operation for radiant as well i.e. 
	on hitting ctrl+O after opening radiant, this should be the location shown on the nav bar. 
	
5) For doing this, once manually open one of the dicom files from the folder "D:\Project Files\DCM FILE"
so that this becomes the default directory of operation for radiant.

# Important
1) After this, first make a folder "Dicom images" in D:\ drive, and run the the code folder.py
which will make folders in this directory with same names as those of the dicom files.

2) Minimise all the other windows (better to close) and run automate.py 

Note: 

1) This code has been written using windows commands, and the python code is run on docker toolbox.
2) Keep all other windows closed while running the code since it may affect the performance speed.
3) Since this code runs by locating images on the screen and keyboard commands, do not interrupt the task in between/Do not perform any other task while the code is running since then the task may remain incomplete.
