# df comes from pandas read_csv.
def pro_weather(df):
    df["time_slice"] = df.Time.map(lambda x:x.split("-")[-1])
    df["date"]=df.Time.map(lambda x:x.split("-")[0]+"-"+x.split("-")[1]+"-"+x.split("-")[2])
    sum_wea = 0.0
    sum_tem = 0.0
    sum_pm = 0.0
    count = 0
    new_df = pd.DateFrame(np.random.randn(144,5),  columns=["date","time_slice","weather","temperature","pm2.5"]
    for i in range(df.shape[0]):
    	sum_wea += df["Weather"].iloc[i]
    	sum_tem += df["temperature"].iloc[i]
    	sum_pm += df["PM2.5"].iloc[i]
    	count += 1

    	if i + 1 == df.shape[0] or not df["time_slice"].iloc[i] == df["time_slice"].iloc[i + 1]:
    		ave_wea = sum_wea / count
    		new_df["time_slice"].iloc[i] = i
    		ave_tem = sum_tem / count 
    		ave_pm = sum_pm / count
    		sum_wea = 0
    		sum_tem = 0
    		sum_pm = 0
    		count = 1
