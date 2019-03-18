#import lib
import requests
import pandas as pd
import time
import config
#assign variables
headers={'Content-Type':'application/xml','QUICKBASE-ACTION':'API_AddRecord'}
ticket=ticket_cred
apptoken=apptoken_cred
#Load excel file
df = pd.read_csv('qb_names.csv',sep=',')
#Clean and format data for API post link
df['Name'] = df['Name'].str.strip().str.replace('\s+','+', regex=True)
df['Price'] = df['Price'].fillna(value=0).astype(str).str.strip()
#Loop to post data to QUICKBASE
for i in range(df['Name'].size):
    name = df.loc[i]['Name']
    price = df.loc[i]['Price']
    r = requests.post('https://mercia.quickbase.com/db/bpf9mbdd2?' +\
     'a=API_AddRecord&' + '_fid_6=' + name + '&_fid_8=' + price + '&ticket='\
     + ticket + '&apptoken=' + apptoken)
    print(r)
    time.sleep(3)
#Notice of script end
print('Upload Completed')
