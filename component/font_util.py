# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/4
Description: font to image
"""

from PIL import Image, ImageFont, ImageDraw

font_style = {
    1: "./font/msyh.ttf",
    2: "./font/msyh_bold.ttf"
}


# Parameters:
# is_bold --> 1: msyh, 2: bold msyh
def transfer_font_to_img(font_text, font_size, back_x, back_y, is_bold):
    font_size = int(font_size)
    back_x = int(back_x)
    back_y = int(back_y)

    # define font
    font = ImageFont.truetype(font_style[is_bold], font_size)
    font_x, font_y = font.getsize(font_text)

    # center the font
    offset_x = (back_x - font_x)/2
    offset_y = (back_y - font_y)/2

    # image with white back-ground color, (255, 255, 255) is white
    back_img = Image.new("RGB", (back_x, back_y), (220, 220, 220))
    draw_brush = ImageDraw.Draw(back_img)
    draw_brush.text((offset_x, offset_y), font_text, font=font, fill="#000000")
    del draw_brush

    return back_img
