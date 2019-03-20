import pandas as pd
df1=pd.read_csv('exercise.csv')
print(df1.columns)
print(df1.head())
df2=pd.read_csv('calories.csv')
print(df2.columns)
print(df2.head())
df3=df2['Calories']
print(df3)
result=pd.concat([df1,df3],axis=1)
print(result.columns)
print(result.head())
result.to_csv('merge.csv')
