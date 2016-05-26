import pandas as pd
import os

def process_weather_dir(needed_map_dir):
    if not os.path.isdir(needed_map_dir) or not os.path.exists(needed_map_dir):
        raise IOError("ERROR: " + needed_map_dir + " not existed or its not a dir")
    print("changeing all the weather... in " + needed_map_dir)
    for file in os.listdir(needed_map_dir):
        if ".csv" in file:
            file_path = os.path.join(needed_map_dir, file)
            print(file)
            # map all the district into concrete value
            mapped_data_frame = process_weather(pd.read_csv(file_path))
            # change the file
            mapped_data_frame.to_csv(file_path, index = False)

def process_weather(data):
    data = data.drop_duplicates(["time"])
    data.reset_index(drop=True,inplace=True)


    dict1 = dict(zip(data.time,data.Weather))
    dict2 = dict(zip(data.time,data["PM2.5"]))
    dict3 = dict(zip(data.time,data["temperature"]))


    date = data["date"].unique()[0]
    week = data["week"].unique()[0]
    

    df = pd.DataFrame(columns=["time","Weather","PM2.5"])
    df["time"]=pd.Series(range(1,145))
    df["Weather"]=0
    df["PM2.5"]=0
    df["temperature"]=0

    df["date"] = date
    df["week"] = week
    default_wea = 0
    default_pm = 0
    default_tem = 0

    for x in df["time"]:
        default_wea = dict1.get(x,default_wea)
        default_pm = dict2.get(x,default_pm)
        default_tem = dict3.get(x,default_tem)

        df["Weather"] = df["Weather"].set_value(int(x)-1,default_wea)
        df["PM2.5"] = df["PM2.5"].set_value(int(x)-1,default_pm)
        df["temperature"] =  df["temperature"].set_value(int(x)-1,default_tem)

    for x in df["time"]:
        if(x>2 and x<143):
      
            s1=df["Weather"][int(x)-1]
            s2=df["Weather"][int(x)+1]
            if(s1 == s2):
                df["Weather"][x]=s1
            else:
                pass
        else:
            pass

    return df

