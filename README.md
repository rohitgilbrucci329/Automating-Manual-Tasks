# Automating-Manual-Tasks

# Instructions for automating:

1) Keep all other windows closed.
2) Do not interrupt the task in between.
3) Specify the directory.
4) Keep all the images on desktop.
5) Directory in which medical images should be there is D:\Project Files\DCM FILE. (Make a directory Project Files and inside which another called DCM FILE)
6) If the directory is to be changed or to be kept the default directory i.e. the one which had been used by radiant the very last time 
 (the one which shows up first when you click ctrl + O), replace its address with "D:\Project Files\DCM FILE" in the code everywhere since my default directory of operation was 
D:\Project Files\DCM FILE where all the dicom files were stored

7) If the code is to remain the same, make sure that this is the directory of operation for radiant as well i.e. 
	on hitting ctrl+O after opening radiant, this should be the location shown on the nav bar. 
	
8) For doing this, once manually open one of the dicom files from the folder "D:\Project Files\DCM FILE"
so that this becomes the default directory of operation for radiant.

Note: This code has been written using windows commands, using docker toolbox.
