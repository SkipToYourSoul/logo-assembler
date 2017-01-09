# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/9
Description: some common functions
"""

import os


def get_abs_path(current_path):
    if not os.path.isabs(current_path):
        return os.path.abspath(current_path)
    else:
        return current_path
