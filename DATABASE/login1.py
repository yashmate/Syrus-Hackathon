import pandas as pd
import numpy as np
def show_details(email):
    df3=df[df['EMAIL']==email]
    print('EMAIL : ',df3['EMAIL'].item())
    print('PASSWORD: ',df3['PASSWORD'].item())
    print('NAME :',df3['NAME'].item())
    print('AGE :',df3['AGE'].item())
    print('SEX : ',df3['SEX'].item())
    print('OCCUPATION : ',df3['OCCUPATION'].item())
email=input('Enter your email')
password=input('Enter password')
df=pd.read_csv('login.csv')
df2=df[df['EMAIL']==email]
if df2.empty:
    print('Invalid EMAIL')
else:
    if df2['PASSWORD'].item()==password:
        print('LOGIN SUCCESSFUL!')
        email=df2['EMAIL'].item()
        show_details(email)
    else:
        print('Invalid Password')


