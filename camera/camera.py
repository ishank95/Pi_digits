#!/usr/bin/env python


from picamera import PiCamera
from time import sleep
import numpy as np
from PIL import Image


def shoot(index):
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/pics/pic%s.jpg' % index)
    camera.stop_preview()
    return flatten_img(index)


def flatten_img(index):
    tmp_img = Image.open('/pics/pic%s.jpg' % index).convert('RGBA')
    arr = np.array(tmp_img)
    print(arr.shape)
    return arr.ravel()


#shoot(1)