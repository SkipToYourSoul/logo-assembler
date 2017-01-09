# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/9
Description: main controller of logo-assembler
"""

import configparser
import traceback
from PIL import Image
import component

backend_image_path = "./pictures/backend/%s.tif"
icon_image_path = "./pictures/icon/%s.tif"

base_image_name = "40×30横（加长49×30）"
main_title = "水火箭的STEM初探"
sub_title = "SCIENCE DREAM"
code_title = "LZ-CM-08-0001"
icon_name = ['图标40×30_0001_防潮', '图标40×30_0002_小心划伤', '图标40×30_0003_破碎', '图标40×30_0004_尖锐物体']
out_path = "./pictures/result.jpg"


def assemble_logo(config_file_name):
    result_image = Image.open(backend_image_path % base_image_name)

    # assemble result image according the config file
    icon_name_flag = 0
    config_dict = get_config(config_file_name)
    for key, value in config_dict.items():
        if key == 'main-title':
            main_title_image = component.transfer_font_to_img(main_title, value['font.size'],
                                                              value['size.x'], value['size.y'], 2)
            result_image = component.assemble_image(result_image, main_title_image,
                                                    value['coordinate.x'], value['coordinate.y'])
        elif key == 'sub-title':
            sub_title_image = component.transfer_font_to_img(sub_title, value['font.size'],
                                                             value['size.x'], value['size.y'], 1)
            result_image = component.assemble_image(result_image, sub_title_image,
                                                    value['coordinate.x'], value['coordinate.y'])
        elif key == 'code128':
            code128_img = component.transfer_to_code128(code_title, int(value['size.y']))
            code128_img = component.resize_image(code128_img, value['size.x'], value['size.y'])
            if value['vertical'] == '1':
                code128_img = component.transpose_image(code128_img)
            result_image = component.assemble_image(result_image, code128_img,
                                                    value['coordinate.x'], value['coordinate.y'])
        elif key == 'footer':
            footer_image = component.transfer_font_to_img(code_title, value['font.size'],
                                                          value['size.x'], value['size.y'], 1)
            if value['vertical'] == '1':
                footer_image = component.transpose_image(footer_image)
            result_image = component.assemble_image(result_image, footer_image,
                                                    value['coordinate.x'], value['coordinate.y'])
        elif key.startswith('icon', 0, 4):
            icon_image = Image.open(icon_image_path % icon_name[icon_name_flag])
            icon_name_flag += 1
            result_image = component.assemble_image(result_image, icon_image,
                                                    value['coordinate.x'], value['coordinate.y'])

    # save result image
    result_image.save(out_path, 'jpeg', quality=95)


def get_config(config_file_name):
    config_dict = {}
    try:
        config_file = configparser.ConfigParser()
        config_path = "./config/%s.conf" % config_file_name
        config_file.read(config_path, "utf-8")
        for section in config_file.sections():
            section_dict = {}
            for key, value in config_file.items(section):
                section_dict[key] = value
            config_dict[section] = section_dict
    except Exception as e:
        traceback.print_exc()
    finally:
        return config_dict

assemble_logo('40x30i4v')
