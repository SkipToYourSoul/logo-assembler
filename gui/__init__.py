# -*- coding:utf-8 -*-

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import traceback
import configparser
from collections import OrderedDict

import component

try:
    import Pmw
    from PIL import Image
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


from gui.gui_component import *
