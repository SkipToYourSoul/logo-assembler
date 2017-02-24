# -*- coding:utf-8 -*-
"""
Author: liye@qiyi.com
Creation Date: 2017/1/9
Description: main controller of logo-assembler
"""
from gui.__init__ import *

backend_image_path = "./pictures/backend/%s.tif"
icon_image_path = "./pictures/icon/%s"


# -------------
#   $1 = main_title 英文标题（String）
#   $2 = sub_title 中文标题（String）
#   $3 = code_title 二维码编号（String）
#   $4 = base_image_name 底图名称（String）
#   $5 = icon_name_list 图标名称数据（List<String>）
#   $6 = output_path 输出路径（String）
# -------------
def assemble_logo(main_title, sub_title, code_title, base_image_name, config_dict, icon_name_list, output_path):
    result_image = Image.open(backend_image_path % base_image_name)

    # assemble result image according the config file
    icon_name_flag = 0
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
                                                          value['size.x'], value['size.y'], 3)
            if value['vertical'] == '1':
                footer_image = component.transpose_image(footer_image)
            result_image = component.assemble_image(result_image, footer_image,
                                                    value['coordinate.x'], value['coordinate.y'])
        elif key.startswith('icon', 0, 4):
            icon_image = Image.open(icon_image_path % icon_name_list[icon_name_flag])
            icon_name_flag += 1
            result_image = component.assemble_image(result_image, icon_image,
                                                    value['coordinate.x'], value['coordinate.y'])

    # save result image
    background_image = Image.new('CMYK', (100, 100))
    result_size = result_image.size
    background_image = background_image.resize(result_size, Image.ANTIALIAS)
    background_image = component.assemble_image(background_image, result_image, 0, 0)
    background_image.save(output_path, format='TIFF', dpi=(300.0, 300.0))
