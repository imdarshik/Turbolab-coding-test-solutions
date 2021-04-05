### Inputs
data_list = [
    {'id':'data1','last_updated':'18-03-2021','frequency':78},
    {'id':'data10','last_updated':'18-03-2021','frequency':96},
    {'id':'data11','last_updated':'17-03-2021','frequency':80},
    {'id':'data2','last_updated':'24-03-2021','frequency':63},
    {'id':'data3','last_updated':'16-03-2021','frequency':61},
    {'id':'data4','last_updated':'22-03-2021','frequency':59},
    {'id':'data5','last_updated':'19-03-2021','frequency':55},
    {'id':'data5','last_updated':'20-03-2021','frequency':78},
    {'id':'data6','last_updated':'17-03-2021','frequency':89},
    {'id':'data6','last_updated':'22-03-2021','frequency':62},
    {'id':'data7','last_updated':'24-03-2021','frequency':82},
    {'id':'data8','last_updated':'21-03-2021','frequency':69},
    {'id':'data9','last_updated':'24-03-2021','frequency':85},
]

from datetime import datetime

### Function to delete in the order of keys
def deletion_order(data_list,priority):
    
    if priority == 'frequency':
        return sorted(
            data_list,
            key = lambda x: (x[priority],datetime.strptime(x['last_updated'], '%d-%m-%Y'))) # Sorts by frequency and date
        
    if priority == 'last_updated':
        return sorted(
            data_list,
            key = lambda x: datetime.strptime(x['last_updated'], '%d-%m-%Y')) # Sorts by date
    
    pass


print(deletion_order(data_list,'frequency'))