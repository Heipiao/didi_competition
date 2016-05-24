#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-20 05:17:06
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: preprocess the data...

## import python`s own lib
import os

## import third party lib
import pandas as pd

## import local lib
from hash_operate import district_hash_map_dir


DATA_DIR = "../../season_1_sad/"

TRAIN_FLAG = True
CONCRETE_DIR = "training_data" if TRAIN_FLAG else "test_set_1"



## all the data dir we want to solve
CLUSTER_MAP_SHEET_DIR = "cluster_map"
ORDER_SHEET_DIR = "order_data"
TRAFFIC_SHEET_DIR = "traffic_data"
WEATHER_SHEET_DIR = "weather_data"
POI_SHEET_DIR = "poi_data"


##############################################################################
###################### analyse weather data here #############################



if __name__ == '__main__':
    map_traffice_district_hash()