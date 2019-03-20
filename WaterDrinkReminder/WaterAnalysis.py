import pandas as pd
import numpy as np
df=pd.read_csv('monthsample.csv')
print(df)
print(df.columns)
#Total water drank during that month\
max_days=df[df['PERCENT']==df['PERCENT'].max()]['DAY']
min_days=df[df['PERCENT']==df['PERCENT'].min()]['DAY']
print('AVERAGE PERCENTAGE COMPLETED')
print(df['PERCENT'].mean())
print('MAX PERCENTAGE COMPLETED')
print(df['PERCENT'].max())
print('MIN PERCENTAGE COMPLETED')
print(df['PERCENT'].min())
print('MEDIAN VALUE IS :')
print(df['PERCENT'].median())
print('YOU DRANK MAXIMUM WATER ON:')
print(max_days.iloc[0])
print('YOU DRANK MINIMUM WATER ON:')
print(min_days.iloc[0])
print('DESCRIPTION:')
print(df.describe(include='all'))
