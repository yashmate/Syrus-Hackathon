import pandas as pd
import numpy as np
def save_to_csv(name,dataframe):
    dataframe.to_csv(name+'.csv')
df=pd.read_csv('yash_mate.csv')
if df.empty:
    df = pd.DataFrame(columns=['Sleep', 'Disease', 'Lasted For','Medications','Causes'])
df2 = pd.DataFrame(columns=['Sleep', 'Disease', 'Lasted For','Medications','Causes'])
n=int(input('Enter the number of entries you want to make'))
for i in range(n):
    sleep=int(input('Enter the number of hours of sleep'))
    disease=input('Enter the name of the disease')
    last=int(input('Duration of disease in days'))
    medications=input('Prescription ')
    cause=input('CAUSES')
    df2.loc[i]=[sleep,disease,last,medications,cause]
    frames=[df,df2]
    result=pd.concat(frames)
    save_to_csv('yash_mate',result)

        

