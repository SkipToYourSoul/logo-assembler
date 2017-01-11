# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/12/28
Description:
"""

from PIL import Image
import component
import gui
from tkinter import *


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)

if __name__ == "__main__":
    # base_image = Image.open('./pictures/test/80×60.tif')
    # part_image = Image.open('./pictures/icon/图标80×60_0001_防潮.tif')
    #
    # result_image = component.assemble_image(base_image, part_image, 261, 449)
    #
    # font_image_1 = component.transfer_font_to_img("水火箭的STEM初探", 40, 568, 55, 2)
    # font_image_2 = component.transfer_font_to_img("LZ-CM-08-0001", 40, 568, 55, 1)
    #
    # result_image = component.assemble_image(result_image, font_image_1, 71, 284)
    # result_image = component.assemble_image(result_image, font_image_2, 71, 339)
    #
    # code128_img = component.transfer_to_code128("LZ-CM-08-0001", 568)
    # code128_img = component.resize_image(code128_img, 568, 72)
    #
    # result_image = component.assemble_image(result_image, code128_img, 71, 756)
    #
    # bottom_image = component.transfer_font_to_img("LZ-CM-08-0001", 20, 568, 24, 1)
    # result_image = component.assemble_image(result_image, bottom_image, 71, 851)
    #
    # result_image.save('./pictures/test.jpg', quality=95)

    root = Tk()
    root.title('Logo-assembler')
    root.resizable(0, 800)
    center_window(root, 400, 620)
    gui.MainContainer(root)
    root.mainloop()
