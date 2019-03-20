import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
app=dash.Dash()
app.layout=html.Div([
    html.H1('BLOOD PRESSURE'),
    dcc.Graph(id='graph'),
    dcc.Interval(id='interval_div',interval=1000,n_intervals=1)
    ])
@app.callback(Output('graph','figure'),
              [Input('interval_div','n_intervals')])
def update_graph(n):
    df=pd.read_csv('gasdata.csv')
    df2=df.iloc[:n]
    data=[go.Scatter(x=df2['Time'],y=df2['Concentration'],
                     mode='markers',
                     marker=dict(color=df['Concentration'],size=df['Concentration']))]
    layout=go.Layout(title='HEART RATE')
    fig=go.Figure(data=data,layout=layout)
    return fig
if __name__=='__main__':
    app.run_server(port=8052)
