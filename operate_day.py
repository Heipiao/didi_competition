def deal_the_day(x):
    if(x.day<10):
        return str(x.year)+'-'+'0'+str(x.month)+'-'+'0'+str(x.day)+'-'+str(x.hour*6+int(x.minute/10)+1)
    else:
        return str(x.year)+'-'+'0'+str(x.month)+'-'+str(x.day)+'-'+str(x.hour*6+int(x.minute/10)+1)