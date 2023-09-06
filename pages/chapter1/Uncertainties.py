from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd  
from datetime import datetime
import plotly.graph_objects as go
import numpy as np

register_page(__name__, icon="ph:squares-four-duotone")

#load data-epistemic
df = pd.read_csv(r"./data/project_data/local_agent_data.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
columns = ['{}_un_epistemic'.format(i) for i in range(int(len(df.columns)/3))]
df = df[columns]
dates = list(df.index)

#load data-aleatoric
df1 = pd.read_csv(r"./data/project_data/local_agent_data.csv")
df1['date'] = pd.to_datetime(df1['date'])
df1 = df1.set_index('date')
columns = ['{}_un_aleatoric'.format(i) for i in range(int(len(df1.columns)/3))]
df1 = df1[columns]


#create slider mark
mark_dict = {}
for i in [int(i * (df.shape[0]-1)/5) for i in range(0,6)]:
    mark_dict[i] = datetime.strftime(df.index[i],'%Y-%m-%d')

def generate_heatmap_eps(start,end):
    tmp = df[start:end].asfreq('D')
    tmp = tmp.bfill()
    values = tmp.asfreq('1W').T
    labels = ['S{}'.format(i+1) for i in range(len(df.columns))]
    #fig = go.Figure(data=[go.Heatmap(x=labels,y = labels, z=values)])
    fig = px.imshow(values,y = labels )
    return fig

def generate_heatmap_alea(start,end):
    tmp = df1[start:end].asfreq('D')
    tmp = tmp.bfill()
    values = tmp.asfreq('1W').T
    labels = ['S{}'.format(i+1) for i in range(len(df1.columns))]
    #fig = go.Figure(data=[go.Heatmap(x=labels,y = labels, z=values)])
    fig = px.imshow(values,y = labels )
    return fig

layout = html.Div(
    [
        dcc.RangeSlider(
            id="date-slider",
            min=0,
            max=len(dates) - 1,
            step=1,
            marks=mark_dict,
        ),
        html.P("Epstemic uncertainty"),
        dcc.Graph(id="heatmaps-graph_eps"),
        html.P("Aleatoric uncertainty"),
        dcc.Graph(id="heatmaps-graph_alea"),
        html.H5("Note: Change company index to real name.."),
        html.H5("Note: Connect to the dashboard's event warning..")
        
        
    ]
)


@callback(Output("heatmaps-graph_eps", "figure"), Input("date-slider", "value"))
def update_heatmap(value):
    if value == None:
        value = [0,len(dates)-1]
    start = dates[value[0]]
    end = dates[value[1]]
    updated_fig = generate_heatmap_eps(start,end)
    return updated_fig

@callback(Output("heatmaps-graph_alea", "figure"), Input("date-slider", "value"))
def update_heatmap1(value):
    if value == None:
        value = [0,len(dates)-1]
    start = dates[value[0]]
    end = dates[value[1]]
    updated_fig = generate_heatmap_alea(start,end)
    return updated_fig


