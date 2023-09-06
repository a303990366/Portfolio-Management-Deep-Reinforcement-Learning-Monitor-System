from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd  
from datetime import datetime
import plotly.graph_objects as go
import numpy as np


register_page(__name__, icon="ph:squares-four-duotone")

#load data
df = pd.read_csv(r"./data/project_data/correlation.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
dates = list(df.index)

#create slider mark
mark_dict = {}
for i in [int(i * (df.shape[0]-1)/5) for i in range(0,6)]:
    mark_dict[i] = datetime.strftime(df.index[i],'%Y-%m-%d')

def generate_heatmap(start,end):
    values = np.array(df[start:end].mean())
    labels = ['S{}'.format(i+1) for i in range(int(len(df.columns)**0.5))]
    values  = values.reshape(len(labels),len(labels))
    #fig = go.Figure(data=[go.Heatmap(x=labels,y = labels, z=values)])
    fig = px.imshow(values,x = labels, y = labels )
    return fig


layout = html.Div(
    [
        html.P("Asset Correlation"),
        dcc.RangeSlider(
            id="date-slider",
            min=0,
            max=len(dates) - 1,
            step=1,
            marks=mark_dict,
            #tooltip={"placement": "bottom", "always_visible": True},
        ),
        dcc.Graph(id="heatmaps-graph_c",figure = generate_heatmap(dates[0],dates[-1]),
            style={"width": "100%", "height": "100%",}),
        html.H5('Note: Change company inde xto real name..'),
        html.H5('Note: Compare stock trend similarity and cosine similarity, If diff too much,warning it..')
    ]
)


@callback(Output("heatmaps-graph_c", "figure"), Input("date-slider", "value"))
def update_heatmap(value):
    if value == None:
        value = [0,len(dates)-1]
    start = dates[value[0]]
    end = dates[value[1]]
    updated_fig = generate_heatmap(start,end)
    return updated_fig