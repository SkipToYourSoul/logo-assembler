# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/12/28
Description:
"""

from PIL import Image


def roll(image, delta):
    # "Roll an image sideways"

    image = image.copy() #复制图像
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image


def thumb_image(origin_image, x, y):
    thumb_size = (x,y)
    origin_image.thumbnail(thumb_size)

    return origin_image


def cut_image(origin_image, left, upper, right, lower):
    tmp_image = origin_image.crop((left, upper, right, lower))
    return  tmp_image


def assemble_image():
    base_image = Image.open('C:/Users/liye/Desktop/base_400_cut.jpg')
    part_image = Image.open('C:/Users/liye/Desktop/part_100_thumb.jpg')

    base_x_size, base_y_size = base_image.size
    part_x_size, part_y_size = part_image.size

    # (left, upper, right, lower)
    # left up
    base_image.paste(part_image, (0, 0, part_x_size, part_y_size))
    # right up
    base_image.paste(part_image, (base_x_size - part_x_size, 0, base_x_size, part_y_size))
    # left down
    base_image.paste(part_image, (0, base_y_size - part_y_size, part_x_size, base_y_size))
    # right down
    base_image.paste(part_image, (base_x_size - part_x_size, base_y_size - part_y_size, base_x_size, base_y_size))

    # center
    base_image.paste(part_image, (150, 150, 250, 250))

    base_image.save('C:/Users/liye/Desktop/complete_1.jpg')



if __name__ == "__main__":
    # image = Image.open('C:/Users/liye/Desktop/base.jpg')

    # delta = 30
    # new_image = roll(image, delta)
    # new_image.save('C:/Users/liye/Desktop/d.jpg')

    # base_image = thumb_image(image, 400, 400)
    # base_image.save('C:/Users/liye/Desktop/base_400.jpg')

    # get base image
    # image1 = Image.open('C:/Users/liye/Desktop/base.jpg')
    # base_image = cut_image(image1, 0, 0, 400, 400)
    # base_image.save('C:/Users/liye/Desktop/base_400_cut.jpg')

    # get part image
    # image2 = Image.open('C:/Users/liye/Desktop/part.jpg')
    # image2_x = thumb_image(image2, 100, 100)
    # image2_x.save('C:/Users/liye/Desktop/part_100_thumb.jpg')

    assemble_image()
