#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-24 23:10:07
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 




## import python`s own lib
import os
import re
from collections import OrderedDict

## import third party lib
import pandas as pd

## import local lib


LOAD_DATA_DIR = "../season_1/"

TRAIN_FLAG = True
CONCRETE_DIR = "training_data" if TRAIN_FLAG else "test_set_1"

POI_SHEET_DIR = "poi_data"

## the line_data is Series style
## 
## --> remove the style is not like this : value#value:value

def remove_error_poi_each_line(line_data):
    ## from 1 to len(..), because the first one is district hash
    ### why I need a temp_line_data here!!!!
    ### Please see the property of the remove() function

    standard_style = re.compile(r"\d+#\d+:\d+")

    line_data = list(line_data[0])
    temp_line_data = line_data.copy()
    for poi_in_line in temp_line_data:
        if len(poi_in_line) == 32: # this is the district hash
            continue
        if not re.match(standard_style, poi_in_line):
            #print(poi_in_line)
            line_data.remove(poi_in_line)
    return pd.Series([line_data])

# the input line_data is a serise!!
def get_district_hash(line_data):
    line_data = list(line_data[0])
    district_hash = line_data[0] # the first one is the district hash
    line_data.remove(district_hash)
    return pd.Series({"district_hash":district_hash, 
                    "pois": line_data})


main_one_sta = dict()
1#11:2241
def get_poi_sta(line_pois):
    this_line_sta = dict()

    for poi in line_pois["pois"]:
        flag_one_p = poi.find("#")
        flag_two_p = poi.find(":")
        main_one = int(poi[:flag_one_p])
        
        main_two = int(poi[flag_one_p + 1 : flag_two_p])

        if not main_one in main_one_sta.keys():
            main_one_sta[main_one] = list()

        # to judeg whether here is a repeat poi data in this line
        if not main_one in this_line_sta.keys():
            this_line_sta[main_one] = list()     
        else:
            if main_two in this_line_sta[main_one]:
                print("error repeat in this line!!!...")
                #print(main_two, main_one_sta[main_one])

        main_one_sta[main_one].append(main_two)
        this_line_sta[main_one].append(main_two)

def arrange_main_pois(main_one_sta):
    for key in main_one_sta.keys():
        main_one_sta[key] = list(set(main_one_sta[key]))

    main_one_sta = OrderedDict(sorted(main_one_sta.items(), key=lambda d:d[0]))


def extract_poi_each_line(line_pois):
    line_pois_map = dict()

    for poi in line_pois["pois"]:
        flag_one_p = poi.find("#")
        flag_two_p = poi.find(":")
        main_one = int(poi[:flag_one_p])
        main_two = int(poi[flag_one_p + 1 : flag_two_p])
        number = int(poi[flag_two_p + 1 :])

        ### we do this because we ensure that:
        #### --> there is no repeat pois each line 
        if not main_one in line_pois_map.keys():
            line_pois_map[main_one] = dict()

        if not main_two in line_pois_map[main_one].keys():
            line_pois_map[main_one][main_two] = number

    # for k, v in line_pois_map.items():
    #     print(k, v)

    # extracted_pos = pd.Series()
    # for k, v in main_one_sta.items():
    #     print(k, v)

    for pos_one in main_one_sta.keys():
        for second in main_one_sta[pos_one]:
            pos_label = str(pos_one) + "_" + str(second)

            if not pos_one in line_pois_map.keys():
                line_pois[pos_label] = 0
                continue
            if not second in line_pois_map[pos_one].keys():
                line_pois[pos_label] = 0
                continue
            line_pois[pos_label] = line_pois_map[pos_one][second]

    return line_pois



def extract_poi_data_normally(poi_df):
    #print(poi_df)
    poi_df.columns = ['raw']
    splited_poi_df = pd.DataFrame(poi_df['raw'].map(lambda x: x.split("\t")))

    ## here we remove the bad poi data
    splited_poi_df = splited_poi_df.apply(remove_error_poi_each_line, axis = 1)
    splited_poi_df.columns = ['raw']

    ## here we distinguish the district hash with pois
    splited_poi_df = splited_poi_df.apply(get_district_hash, axis = 1)
    #print(splited_poi_df["district_hash"])
    ## here we statistic the info about poi
    splited_poi_df.apply(get_poi_sta, axis = 1)
    arrange_main_pois(main_one_sta)

    # sum_ = 0
    # for k, v in main_one_sta.items():
    #     print(k, v)
    #     sum_ += len(v)
    # print(sum_)

    splited_poi_df = splited_poi_df.apply(extract_poi_each_line, axis = 1)
    splited_poi_df.drop("pois", axis=1, inplace=True)

    return splited_poi_df






if __name__ == '__main__':
    poi_data_path = os.path.join(LOAD_DATA_DIR, CONCRETE_DIR, POI_SHEET_DIR, "poi_data")
    poi_df = pd.read_csv(poi_data_path,header=-1)
    normal_poi_df = extract_poi_data_normally(poi_df)
    print(normal_poi_df.columns)
    print(normal_poi_df.shape)
    print(normal_poi_df.head())
