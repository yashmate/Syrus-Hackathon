import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('sleep.csv')
print(df.columns)
print(df)
trace1 = go.Bar(
    x=df['SleepDay'],  # NOC stands for National Olympic Committee
    y=df['TotalMinutesAsleep'],
    name = 'Asleep',
    marker=dict(color='#FFD700') # set the marker color to gold
)
trace2 = go.Bar(
    x=df['SleepDay'],
    y=df['TotalTimeInBed'],
    name='TotalTime',
    marker=dict(color='#9EA0A1') # set the marker color to silver
)
data = [trace1, trace2]
layout = go.Layout(
    title='Sleep Cycle'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='sleepcycle.html')
