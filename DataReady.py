from PIL import Image
import glob
import os
import datetime

#  Date-Time-FrameNumber-CameraSerialNum-Front/Rear.png

out_dir = input("Enter your destination folder you want to save PNG image ")
bmp_img_path = input("Enter your BMP file folder ")
bmp_img_path = bmp_img_path +'/*.bmp'
CameraSerialNum = input("Enter Camera Serial Number (if you dont know, enter nothing!)")
FR = ''
FrameNumber = 1
x = datetime.datetime.now()
year = x.strftime("%Y")
month = x.strftime("%m")
day = x.strftime("%d")
hour = x.strftime("%H")
minute = x.strftime("%M")
second = x.strftime("%S")
milisecond = str(int(x.strftime("%f"))//1000)

FrameNumber = 1
for img in glob.glob(bmp_img_path):
    if '-f' in img:
        FR = '-f'
    elif '-r' in img:
        FR = '-r'
    else:
        FR = '-NONE'
    image_name = year + month + day + '-' + hour + minute + second + milisecond + '-' + str(FrameNumber) + FR
    Image.open(img).save(os.path.join(out_dir, image_name + '.png'))
    FrameNumber += 1

