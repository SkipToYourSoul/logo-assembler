# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/4
Description: generate QRcode(code128)
"""

from component.__init__ import *


def transfer_to_code128(text, height=100):
    code128_image = code128.image(text, height)
    return code128_image
