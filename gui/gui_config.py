# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/11
Description: get config data
"""
from gui.__init__ import *

base_config_path = "./config"


# get notice icon from icon.conf
def get_icon_config():
    icon_setting = []
    row = 0
    column = 0
    for line in open('%s/icon.conf' % base_config_path, 'r', encoding='utf-8'):
        if not line.strip().startswith('#') and not line.strip() == "":
            icon = line.strip()
            icon_setting.append((icon, row, column))
            column += 1
            if column % 3 == 0:
                row += 1
                column = 0
    return icon_setting


# get backend image from backend.conf
def get_backend_config():
    backend_setting = []
    for line in open('%s/backend.conf' % base_config_path, 'r', encoding='utf-8'):
        if not line.strip().startswith('#') and not line.strip() == "":
            backend_setting.append(line.strip())
    return tuple(backend_setting)


# get icon count from icon_count.conf
def get_icon_count_config():
    icon_count_setting = []
    for line in open('%s/icon_count.conf' % base_config_path, 'r', encoding='utf-8'):
        if not line.strip().startswith('#') and not line.strip() == "":
            icon_count_setting.append(line.strip())
    return tuple(icon_count_setting)


# get logo config according the file name
def get_logo_config(config_file_name):
    config_dict = OrderedDict()
    try:
        config_file = configparser.ConfigParser()
        config_path = "%s/%s" % (base_config_path, config_file_name)
        config_file.read(config_path, "utf-8")
        for section in config_file.sections():
            section_dict = {}
            for key, value in config_file.items(section):
                section_dict[key] = value
            config_dict[section] = section_dict
    except Exception as e:
        traceback.print_exc()
        config_dict = {}
    finally:
        return config_dict
