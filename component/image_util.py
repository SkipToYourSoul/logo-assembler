# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/4
Description: Some basic utils to handle image
"""
from component.__init__ import *


# rotate a image according the angle
def transpose_image(current_image):
    tmp_image = current_image.transpose(Image.ROTATE_90)
    return tmp_image


# resize a image according the size
def resize_image(current_image, x, y):
    x = int(x)
    y = int(y)
    coordinate = (x, y)
    tmp_image = current_image.resize(coordinate, Image.ANTIALIAS)
    return tmp_image


# make thumb image according the size
def thumb_image(current_image, x, y):
    x = int(x)
    y = int(y)
    thumb_size = (x, y)
    tmp_image = current_image.thumbnail(thumb_size, Image.ANTIALIAS)
    return tmp_image


# cut the image according the coordinate
def cut_image(current_image, coordinate):
    # coordinate = (left, upper, right, lower)
    tmp_image = current_image.crop(coordinate)
    return tmp_image


# put the part_image to base_image
#   x, y: the coordinate of part_image
def assemble_image(base_image, part_image, x, y):
    base_x_size, base_y_size = base_image.size
    part_x_size, part_y_size = part_image.size
    x = int(x)
    y = int(y)

    if base_x_size < part_x_size or base_y_size < part_y_size:
        return base_image

    base_image.paste(part_image, (x, y, x + part_x_size, y + part_y_size))

    return base_image
