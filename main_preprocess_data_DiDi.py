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
from operate_hash import district_hash_map_dir
from operate_weather_data import process_weather_dir
from operate_order_sheet import process_order_data_dir


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
###################### preprocess traffic data here ##########################
def map_traffice_district_hash():
    traffic_data_dir = os.path.join(DATA_DIR, CONCRETE_DIR, TRAFFIC_SHEET_DIR)
    # map the 
    district_hash_map_dir(traffic_data_dir)

def process_weather_noise():
	weather_data_dir = os.path.join(DATA_DIR, CONCRETE_DIR, WEATHER_SHEET_DIR)
	process_weather_dir(weather_data_dir)

def map_order_data_district_hash():
    order_data_dir = os.path.join(DATA_DIR, CONCRETE_DIR, ORDER_SHEET_DIR)
    district_hash_map_dir(order_data_dir)

def process_order_sheet():
	order_data_dir = os.path.join(DATA_DIR, CONCRETE_DIR, ORDER_SHEET_DIR)
	process_order_data_dir(order_data_dir)







if __name__ == '__main__':
    # map_traffice_district_hash()
    #process_weather_noise()
    map_order_data_district_hash()
    process_order_sheet()


