import plotly.graph_objs as go
import plotly.offline as pyo
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
df=pd.read_csv('gasdata.csv')
app=dash.Dash()
app.layout=html.Div([
    dcc.Graph(id='graph'),
    dcc.Interval(id='interval-div',interval=750,n_intervals=1),

    ])
@app.callback(Output('graph','figure'),[Input('interval-div','n_intervals')])
def update(n):
    df2=df.iloc[:n]
    y_new=df2['Concentration'].iloc[-1]
    trace1=go.Bar(x=['Heart-Rate'],y=[y_new],width=0.1,marker=dict(color='green'),
                  opacity=0.6)
    trace2=go.Bar(x=['Heart-Rate'],y=[y_new],width=0.1,marker=dict(color='red'),
                  opacity=0.6)
    if y_new > 50:
        trace= trace2
    else:
        trace=trace1
    data=[trace]
    layout=go.Layout(title='Updating Bar Chart',yaxis=dict(range=[0,150]),
                     xaxis=dict(range=[-1,1]),
                     plot_bgcolor='rgba(204, 179, 255,0.5)')
    fig=go.Figure(data=data,layout=layout)
    return fig
    
if __name__=='__main__':
    app.run_server()

