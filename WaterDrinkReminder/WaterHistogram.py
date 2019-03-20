import random
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
percent=np.random.randint(0,101,12)
days=list(range(1,13))
data = [go.Bar(
    x=days,  
    y=percent
)]
layout = go.Layout(
    title='Water Intake During March'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='water1.html')

