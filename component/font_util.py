# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/4
Description: font to image
"""

from component.__init__ import *

font_style = {
    1: "./font/msyh.ttf",
    2: "./font/msyh_bold.ttf",
    3: "./font/arial.ttf"
}


# Parameters:
# is_bold --> 1: msyh, 2: bold msyh, 3: arial
def transfer_font_to_img(font_text, font_size, back_x, back_y, is_bold):
    font_size = int(font_size)
    back_x = int(back_x)
    back_y = int(back_y)

    # define font
    font = ImageFont.truetype(font_style[is_bold], font_size)
    font_x, font_y = font.getsize(font_text)

    # while font_x > back_x:
    #     font_size -= 1
    #     font = ImageFont.truetype(font_style[is_bold], font_size)
    #     font_x, font_y = font.getsize(font_text)

    if font_x <= back_x:
        # center the font
        offset_x = (back_x - font_x)/2
        # offset_y = (back_y - font_y)/2
        offset_y = 0

        # image with white back-ground color, (255, 255, 255) is white
        back_img = Image.new("CMYK", (back_x, back_y))
        draw_brush = ImageDraw.Draw(back_img)
        draw_brush.text((offset_x, offset_y), font_text, font=font, fill="#000000")
        del draw_brush
    else:
        back_img = Image.new("CMYK", (font_x, back_y))
        draw_brush = ImageDraw.Draw(back_img)
        draw_brush.text((0, 0), font_text, font=font, fill="#000000")
        back_img = back_img.resize((back_x, back_y), Image.ANTIALIAS)
        del draw_brush

    return back_img
