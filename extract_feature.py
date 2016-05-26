import pandas as pd


def extract_weather_order(needed_dir1,needed_dir2):
    if not os.path.isdir(needed_map_dir1) or not os.path.exists(needed_map_dir1):
        raise IOError("ERROR: " + needed_map_dir1 + " not existed or its not a dir")
    if not os.path.isdir(needed_map_dir2) or not os.path.exists(needed_map_dir2):
        raise IOError("ERROR: " + needed_map_dir2 + " not existed or its not a dir")
    print("combine two path " + needed_map_dir1+" and "+needed_dir2 )
    for file in os.listdir(needed_map_dir):
        if ".csv" in file:
            file_path = os.path.join(needed_map_dir, file)
           
            # map all the district into concrete value
            mapped_data_frame = process_weather(pd.read_csv(file_path))
            # change the file
            mapped_data_frame.to_csv(file_path, index = False)

def extract_weather_order_dir():
    weather 