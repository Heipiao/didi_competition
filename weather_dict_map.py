data = pd.DataFrame(columns = ["time_slice"])
data["time_slice"] = pd.Series((range(1,145))


default = 0
def unique_weather(df):
    dict1 = dict(zip(df.time,df.weather))
    for x in data["time_slice"]:
    	data = dict1.get(x,default)




# remove the repeat time data
# remove the noise time data
def is_noise(df, i):
	y = 5


 def clean_weather_data(df):
    #removed_repeat_data = df.drop_duplicates(["time"])
    
