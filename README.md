# Rename_Images
the exe file which rename all bmp images in a folder in "Date-Time-FrameNumber-CameraSerialNum-Front/Rear.png" format  and convert to png

## create .exe file in ubunto

Step 1: 
Install the library pyinstaller. pip3 install pyinstaller

Step 2: 
Go into the directory of your ‘.py’ file

Step 3: 
pyinstaller --onefile -w 'filename.py'
Here the ‘.py’ file name is ‘DataReady’.

you can find the exe file in folder named "dist".
