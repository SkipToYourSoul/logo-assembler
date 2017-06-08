# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/4
Description: import the base component
"""

try:
    import Pmw
    from PIL import Image, ImageFont, ImageDraw
    import code128
except ImportError:
    import sys
    print(sys.stderr, """ !!!
    There was a problem importing one of the Python modules required.
    The error leading to this problem was:
    %s

    Please install a package which provides this module, or verify that the module is installed correctly.
    It's possible that the above module doesn't match the current version of Python, which is:
    %s

    """) % (sys.exc_info(), sys.version)
    sys.exit(1)



from component.image_util import *
from component.font_util import *
from component.code128_util import *
