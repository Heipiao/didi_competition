#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-19 01:51:41
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 

import os

import re


def is_required_file(file_name, style, is_add):
    """ make sure the file does not have a concrete style """
    if is_add:
        return False if "."+style in file_name else True
    else:
        return True if "."+style in file_name else False


def add_style_suffix(file_name, style):
    """ add the style we want to the end of the file """
    return file_name + "." + style # add style

def remove_style_suffix(file_name, style):
    """ remove the .style suffix in the file_name """
    return file_name[:file_name.index(style) - 1]

## Other parameters is obvious 
## is_add : True -->  add the file_style into all the file
##        : False --> remove file_style from all the file 
def operate_file_style(file_style = "csv", bases_dir = "../season_1/", is_add = True):
    """ add the style into the none style files """
    if not os.path.exists(bases_dir):
        raise IOError("Path is not existed!...")
    if not os.path.isdir(bases_dir):
        raise IOError("This is not a dir!...")

    files = os.listdir(bases_dir)
    for file in files:
        file_path = os.path.join(bases_dir, file)
        if os.path.isdir(file_path):
            operate_file_style(file_style, file_path, is_add)
        else:
            if is_required_file(file, file_style, is_add):
                new_file = add_style_suffix(file, file_style) \
                                if is_add else remove_style_suffix(file, file_style)
                new_file_path = os.path.join(bases_dir, new_file)
                os.rename(file_path, new_file_path)

if __name__ == '__main__':
    operate_file_style(is_add = True, bases_dir = "../season_1_sad/")

