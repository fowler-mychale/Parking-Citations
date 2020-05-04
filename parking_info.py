import pandas as pd
import numpy as np
import time
import datetime

df = pd.read_csv('C:/Users/Mike_F/Desktop/Parking_Citations2.csv')   

df.drop(['Ticket number'],axis = 1, inplace = True)

df['Issue Date']= pd.to_datetime(df['Issue Date']) 

df['Month'] = df['Issue Date'].apply(lambda date: date.month)
df['Year'] = df['Issue Date'].apply(lambda date: date.year)

df.drop(['Issue Date'],axis = 1, inplace = True)

#fill null data with 0
df.fillna(0, inplace=True)


pd.DataFrame.to_csv(df,"" + time.strftime('Ticket %Y-%m-%d') + ".csv",',')
