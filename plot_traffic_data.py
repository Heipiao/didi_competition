#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-23 07:07:48
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 




## import python`s own lib
import os

## import third party lib
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

## import local lib

# import matplotlib
# matplotlib.use('MacOSX')

DATA_DIR = "../../season_1_sad/" # only change this dir to change the operate dir

TRAIN_FLAG = True
CONCRETE_DIR = "training_data" if TRAIN_FLAG else "test_set_1"


TRAFFIC_SHEET_DIR = "traffic_data"


# tj_level1_count  tj_level2_count  tj_level3_count tj_level4_count
# week  date  time  district
# Axes3D.scatter(xs, ys, zs=0, zdir='z', s=20, c='b', *args, **kwargs)
def plot_single_day_traffic(df):
    y_tj_l1 = df["tj_level1_count"]
    y_tj_l2 = df["tj_level2_count"]
    y_tj_l3 = df["tj_level3_count"]
    y_tj_l4 = df["tj_level4_count"]

    x_time = df["time"]
    x_district = df["district"]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_time, x_district, y_tj_l1, )
    #ax.plot_surface(x_time, x_district, y_tj_l1)
    print(plt.get_backend())
    plt.show()
    plt.savefig("plot_traffic.png")
    

if __name__ == '__main__':
    file = "traffic_data_2016-01-01.csv"
    path = os.path.join(DATA_DIR, CONCRETE_DIR, TRAFFIC_SHEET_DIR, file)
    df = pd.read_csv(path)
    print(df)
    #plot_single_day_traffic(df)
    uni_x = df["time"].unique()
    a = np.argsort(uni_x)
    print(uni_x[a])
