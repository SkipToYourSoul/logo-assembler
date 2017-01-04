# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/4
Description: font to image
"""

import os
from PIL import Image, ImageFont, ImageDraw

# msyh.ttf: 微软雅黑
# simsun.ttc: 宋体

# Image.new('RGB',(width,height),background_color)

text = u"这是一段测试文本，test 123。"

im = Image.new("RGB", (300, 50), (255, 255, 255))
dr = ImageDraw.Draw(im)

# font_path = os.path.join("fonts", "msyh.ttf")

font_path = "../font/msyh.ttf"
bold_font_path = "../font/msyh_bold.ttf"

font = ImageFont.truetype(bold_font_path, 14)

dr.text((10, 5), text, font=font, fill="#000000")

# im.show()
im.save("t2.png")
