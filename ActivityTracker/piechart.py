import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as pyo

labels = ['Sleeping','Studying','Excercise','Eating','Sitting','Walking']
values = [9,3,1,3,6,2]

trace = go.Pie(labels=labels, values=values)

pyo.plot([trace], filename='basic_pie_chart.html')
