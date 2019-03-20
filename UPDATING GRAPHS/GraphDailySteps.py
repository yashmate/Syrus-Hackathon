import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import plotly.offline as pyo
df=pd.read_csv('dailysteps.csv')
print(df)
trace0 = go.Bar(
    x = df['ActivityDay'],
    y = df['StepTotal'],
    name = 'markers'
)

data = [trace0]
layout = go.Layout(
    title = 'Line chart showing three different modes'
)
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='dailystepsbar.html')
