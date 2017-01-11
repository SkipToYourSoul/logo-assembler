# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2016/12/28
Description:
"""

import gui
from tkinter import *


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)

if __name__ == "__main__":
    root = Tk()
    root.title('Logo-assembler')
    root.resizable(0, 800)
    center_window(root, 400, 620)
    gui.MainContainer(root)
    root.mainloop()
