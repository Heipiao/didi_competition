import pandas as pd

from extract_feature import extract_weather_order_dir

DATA_DIR_PATH = "../../season_1_sad/"

TRAIN_FLAG = True
CONCRETE_DIR = "training_data" if TRAIN_FLAG else "test_set_1"

# all the data dir we want to solve
CLUSTER_MAP_SHEET_DIR = "cluster_map"
ORDER_SHEET_DIR = "order_data"
TRAFFIC_SHEET_DIR = "traffic_data"
WEATHER_SHEET_DIR = "weather_data"
POI_SHEET_DIR = "poi_data"

def Combine_weather_order():
    weather_data_dir = os.path.join(DATA_DIR, CONCRETE_DIR, WEATHER_SHEET_DIR)
    order_data_dir = os.path.join(DATA_DIR, CONCRETE_DIR, ORDER_SHEET_DIR)
    # map the 
    extract_weather_order_dir(weather_data_dir,order_data_dir)