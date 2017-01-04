# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/4
Description: generate QRcode(code128)
"""

import code128

code128.image("LZ-CM-08-0001").save("LZ-CM-08-0001.png")


def transfer_to_code128(text, output_path, height=100):
    code128_image = code128.image(text, height)
    code128_image.save(output_path)


def transfer_to_code128(text, height=100):
    code128_image = code128.image(text)
    return code128_image
