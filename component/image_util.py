# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/4
Description: Some basic utils to handle image
"""

from PIL import Image
import os


# resize a image according the size
def resize_image(current_image, x, y):
    coordinate = (x, y)
    current_image.resize(coordinate)


# make thumb image according the size
def thumb_image(current_image, x, y):
    thumb_size = (x, y)
    tmp_image = current_image.thumbnail(thumb_size)
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

    if base_x_size < part_x_size or base_y_size < part_y_size:
        return base_image

    base_image.paste(part_image, (x, y, x + part_x_size, y + part_y_size))

    return base_image


def get_abs_path(current_path):
    if not os.path.isabs(current_path):
        return os.path.abspath(current_path)
    else:
        return current_path

if __name__ == '__main__':
    base_image = Image.open(get_abs_path('../jpgs/40×30.jpg'))
    part_image = Image.open('../jpgs/1.jpg')

    result = assemble_image(base_image, part_image, 261, 449)
    result.save('../jpgs/result×1.jpg')
