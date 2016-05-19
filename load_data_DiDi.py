import pandas as pd
import os

# handle the order_info sheet
def order_sheet_pre():
#set filename and input data
    print("load data from:")
    for x in range(START,END,SEP):
        syspath = "../../season_1/"+IS_TRAINING+"/order_data/"
        if(x<10):
            name = "order_data_2016-01-0"+str(x)+_TEST
        else:
            name = "order_data_2016-01-"+str(x)+_TEST
        print(name)
        data = pd.read_csv(os.path.join(syspath,name),header=-1)
        
#processing data and slice time 
        print("process data...")
        data.columns = ['raw']
        data['order_id'] = data['raw'].map(lambda x: x.split("\t")[0])
        data['driver_id'] = data['raw'].map(lambda x: x.split("\t")[1])
        data['passenger_id'] = data['raw'].map(lambda x: x.split("\t")[2])
        data['start_district_hash'] = data['raw'].map(lambda x: x.split("\t")[3])
        data['dest_district_hash'] = data['raw'].map(lambda x: x.split("\t")[4])
        data['Price'] = data['raw'].map(lambda x: x.split("\t")[5])
        data['Time'] = data['raw'].map(lambda x: x.split("\t")[6])
        t = pd.to_datetime(data['Time'])
        data['Time']=t.map(lambda x:str(x.year)+'-'+str(x.month)+'-'+str(x.day)+'-'+str(x.hour*6+int(x.minute/10)+1))
        del data['raw']#del useless column

#save as the specific dir
        save_path ="../../season_1_sad/"+IS_TRAINING+"/order_data/"
        if os.path.isdir(save_path):
            print("save data at"+save_path+name)
            data.to_csv(os.path.join(save_path,name))
        else:
            os.makedirs(save_path)
            print("save data at"+save_path+name)
            data.to_csv(os.path.join(save_path,name))

def traffic_sheet_pre():
#set filename and input data
    print("load data from:")
    for x in range(START,END,SEP):
        syspath = "../../season_1/"+IS_TRAINING+"/traffic_data/"
        if(x<10):
            name = "traffic_data_2016-01-0"+str(x)+_TEST
        else:
            name = "traffic_data_2016-01-"+str(x)+_TEST
        print(name)
        data = pd.read_csv(os.path.join(syspath,name),header=-1)
        
#processing data and slice time 
        print("process data...")
        data.columns = ['raw']
        data['district_hash'] = data['raw'].map(lambda x: x.split("\t")[0])
        data['tj_level1_count'] = data['raw'].map(lambda x: x.split("\t")[1][2:])
        data['tj_level2_count'] = data['raw'].map(lambda x: x.split("\t")[2][2:])
        data['tj_level3_count'] = data['raw'].map(lambda x: x.split("\t")[3][2:])
        data['tj_level4_count'] = data['raw'].map(lambda x: x.split("\t")[4][2:])
        data['tj_time'] = data['raw'].map(lambda x: x.split("\t")[5])
        t = pd.to_datetime(data['tj_time'])
        data['tj_time']=t.map(lambda x:str(x.year)+'-'+str(x.month)+'-'+str(x.day)+'-'+str(x.hour*6+int(x.minute/10)+1))
        del data['raw']#del useless column

#save as the specific dir
        save_path ="../../season_1_sad/"+IS_TRAINING+"/traffic_data/"
        if os.path.isdir(save_path):
            print("save data at"+save_path+name)
            data.to_csv(os.path.join(save_path,name))
        else:
            os.makedirs(save_path)
            print("save data at"+save_path+name)
            data.to_csv(os.path.join(save_path,name))


def weather_sheet_pre():
#set filename and input data
    print("load data from:")
    for x in range(START,END,SEP):
        syspath = "../../season_1/"+IS_TRAINING+"/weather_data/"
        if(x<10):
            name = "weather_data_2016-01-0"+str(x)+_TEST
        else:
            name = "weather_data_2016-01-"+str(x)+_TEST
        print(name)
        data = pd.read_csv(os.path.join(syspath,name),header=-1)
        
#processing data and slice time 
        print("process data...")
        data.columns = ['raw']
        data['Time'] = data['raw'].map(lambda x: x.split("\t")[0])
        t = pd.to_datetime(data['Time'])
        data['Time']=t.map(lambda x:str(x.year)+'-'+str(x.month)+'-'+str(x.day)+'-'+str(x.hour*6+int(x.minute/10)+1))
        data['Weather'] = data['raw'].map(lambda x: x.split("\t")[1])
        data['temperature'] = data['raw'].map(lambda x: x.split("\t")[2])
        data['PM2.5'] = data['raw'].map(lambda x: x.split("\t")[3])
        del data['raw']#del useless column

#save as the specific dir
        save_path ="../../season_1_sad/"+IS_TRAINING+"/weather_data/"
        if os.path.isdir(save_path):
            print("save data at"+save_path+name)
            data.to_csv(os.path.join(save_path,name))
        else:
            os.makedirs(save_path)
            print("save data at"+save_path+name)
            data.to_csv(os.path.join(save_path,name))

if __name__ == '__main__':
    while True:
        choice = input("test or train?")
        if (choice == 'test'):
            IS_TRAINING = "test_set_1"
            START = 22
            END   = 32
            SEP   = 2
            _TEST = '_test'
            break
        elif(choice == 'train'):
            IS_TRAINING = "training_data"
            START = 1
            END = 22
            SEP = 1
            _TEST = ''
            break
        else:
            print("just answer test or train directly !!")
    
    order_sheet_pre()
    traffic_sheet_pre()
    weather_sheet_pre()


