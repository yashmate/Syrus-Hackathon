import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
df=pd.read_csv('gasdata.csv')
app=dash.Dash()
print(df.columns)
app.layout=html.Div([
    dcc.Graph(id='graph'),
    dcc.Interval(id='interval-div',interval=1000,n_intervals=0)
    ])
@app.callback(Output('graph','figure'),[Input('interval-div','n_intervals')])
def update_graph(n):
    data=[go.Bar(x=df['Time'],y=df['Concentration'])]
    layout=go.Layout('Gas Concentrations')
    fig=go.Figure(data=data,layout=layout)
    return fig
if __name__=='__main__':
    app.run_server()
