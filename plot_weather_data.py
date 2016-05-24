import pandas as pd

from operate_plot_weather import plot_single_day_weather

data = pd.read_csv("../../season_1_sad/training_data/weather_data/weather_data_2016-01-06.csv")
data = data.drop_duplicates(["time"])
data.reset_index(drop=True,inplace=True)


dict1 = dict(zip(data.time,data.Weather))
dict2 = dict(zip(data.time,data["PM2.5"]))
dict3 = dict(zip(data.time,data["temperature"]))

df = pd.DataFrame(columns=["time","Weather","PM2.5"])
df["time"]=pd.Series(range(1,145))
df["Weather"]=0
df["PM2.5"]=0
df["temperature"]=0
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

plot_single_day_weather(df)