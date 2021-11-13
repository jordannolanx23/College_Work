"""
Created on Thr Feb  27:4:00pm 2020

@author: nolan
"""

from PIL import Image
import numpy as np

im = np.array(Image.open('cat.png'))

print(im.dtype)
# uint8

print(im.ndim)
# 3

print(im.shape)
# (590, 683, 3)

print(im[256, 256])
# print RGB values of image at location[x,y]
# [143,128,152]

## to save example ##
#pil_img = Image.fromarray(im)
#pil_img.save('blood_save.png')

# inverse and test save #
im_i = 255 - im
Image.fromarray(im_i).save('cat_inverse.png')
print('save successful')
