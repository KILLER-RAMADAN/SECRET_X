import png
import pyqrcode
import os
import shutil
title = input("give your qr code a title!>>")
text = input("what would you like the qr_code to say ?")
file_name_png = title+".png"
url = pyqrcode.create(text)
url.png(file_name_png, scale=10)
os.makedirs(fr"c://Users//ahmed//Desktop//{title}")
shutil.move(f"{file_name_png}", fr"c://Users//ahmed//Desktop//{title}")
