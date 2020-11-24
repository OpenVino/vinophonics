#!/usr/bin/python3

import time
import os

def image_capture ():
        try:
             os.system('gphoto2 --capture-image-and-download --filename "/threesixty/vinofisheye.jpg" --force-overwrite --camera "Canon EOS 600D"')
        except Exception as error:
             print("An exception ocurred with gphoto {error}")
while True:
        image_capture()
        time.sleep(60)
