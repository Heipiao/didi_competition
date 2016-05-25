import pandas as pd
import os

def process_order_data_dir(needed_map_dir):
    if not os.path.isdir(needed_map_dir) or not os.path.exists(needed_map_dir):
        raise IOError("ERROR: " + needed_map_dir + " not existed or its not a dir")
    print("change order sheet... in " + needed_map_dir)
    for file in os.listdir(needed_map_dir):
        if ".csv" in file:
            file_path = os.path.join(needed_map_dir, file)
            print(file)
            # map all the district into concrete value
            mapped_data_frame = process_order_data(pd.read_csv(file_path))
            # change the file
            mapped_data_frame.to_csv(file_path, index = True)

def process_order_data(data):
    data["NULL"] = data["driver_id"].isnull()

    df = pd.DataFrame(columns=["order_count","null_count","fee_sum"])

    grouped = data.groupby(["Time","start_district"], sort=True)
    df["order_count"] = grouped.count()["dest_district"]
    df["null_count"] = grouped.sum()["NULL"].astype(int)
    df["fee_sum"] = grouped.sum()["Price"]
     
    return df

    