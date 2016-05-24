#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-20 05:17:06
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
# #plt.title("single daya " + str(df["date"].unique()[0]) + " Week-" + str(df["week"].unique()[0]) + " weather")

# @Description: preprocess the data...

## import python`s own lib
import os

## import third party lib
import pandas as pd
import matplotlib.pyplot as plt
## import local lib



DATA_DIR = "../../season_1_sad/"

TRAIN_FLAG = True
CONCRETE_DIR = "training_data" if TRAIN_FLAG else "test_set_1"


WEATHER_SHEET_DIR = "weather_data"


def plot_single_day_weather(df):
    y_pm = df["PM2.5"]
    y_wea = df["Weather"]
    y_tem = df["temperature"] 

    x = df["time"]  

    plt.figure(figsize=(8,7),dpi=98)
    


    p_pm = plt.subplot(311)
    p_pm.set_ylabel("PM2.5")
    #p_pm.set_xlabel("time_slice")
    p_pm.grid(True)
    p_pm.axis([0, 150, 0, y_pm.max() + 5])
   
    p_wea = plt.subplot(312)
    p_wea.set_ylabel("Weather")
    p_wea.axis([0, 150, 0, y_wea.max() + 1])
    #p_wea.set_xlabel("time_slice")
    p_wea.grid(True)

    p_tem = plt.subplot(313)
    p_tem.set_ylabel("tenperature")
    p_tem.set_xlabel("time_slice")
    p_tem.axis([0, 150, 0, y_tem.max() + 1])
    p_tem.grid(True)

    p_pm.plot(x, y_pm,"g-",label="PM2.5")
    p_wea.scatter(x, y_wea,label="weather_data",linewidth=2) 
    p_tem.plot(x, y_tem,"b.",label="temperature",linewidth=2)


    plt.show()

 # def plot_pre_week(df,n):
 # 	n_start = n*7*144
 #    n_end   = (n+1)*7*144
 #    y_pm = df["PM2.5"][n_start:n_end]
 #    y_wea = df["Weather"][n_start:n_end]
 #    y_tem = df["temperature"][n_start:n_end]

 #    x = df["time"]  

if __name__ == '__main__':
    df = pd.read_csv("../../season_1_sad/training_data/weather_data/weather_data_2016-01-01.csv")
    plot_single_day_weather(df)
    