#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-21 20:51:38
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 

## import python`s own lib
import os

## import third party lib
import pandas as pd




# the data should be DataFrame from pandas
def save_df_to_file(data, save_path, file):
    saved_file = os.path.join(save_path, file)
    if os.path.isdir(save_path):
        data.to_csv(saved_file, index = False)
    else:
        os.makedirs(save_path)
        data.to_csv(saved_file, index = False)
