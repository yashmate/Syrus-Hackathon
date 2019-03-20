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
    df_trace1=df2[df2['Concentration']>50]
    trace1=go.Scatter(x=df_trace1['Time'],y=df_trace1['Concentration'],
                      mode='markers',marker=dict(color='green'))
    
    trace2=go.Scatter(x=df2['Time'],y=df2['Concentration'],
                     mode='lines',
                     marker=dict(color='#8B008B'))
    data=[trace2,trace1]
    layout=go.Layout(title='BLOOD PRESSURE GRAPH')
    fig=go.Figure(data=data,layout=layout)
    return fig
if __name__=='__main__':
    app.run_server(port=8053)
