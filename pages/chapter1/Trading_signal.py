from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px
from datetime import datetime
import plotly.graph_objects as go
import numpy as np
import pandas as pd


register_page(__name__, icon="fa:bar-chart")

#load data
df = pd.read_csv("./data/project_data/local_agent_data.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
columns = ['{}_action'.format(i) for i in range(int(len(df.columns)/3))]
df = df[columns]
dates = list(df.index)

#create slider mark
mark_dict = {}
for i in [int(i * (df.shape[0]-1)/5) for i in range(0,6)]:
    mark_dict[i] = datetime.strftime(df.index[i],'%Y-%m-%d')


def generate_bar(start,end):
    #1 is buy, 0 is sell
    tmp = df[start:end]
    values = tmp[tmp==1].isna().sum()# how many 0 times
    values = values.to_frame()
    values.columns = ['Selling']
    values['Buying'] = df.shape[0] - values['Selling']

    fig = px.bar(values,orientation='h')
    fig.update_layout(
        xaxis_title="Stock",  # Set x-label
        yaxis_title="Ratio",  # Set y-label
    )
    return fig

#, x="Stock", y="Ratio", color="smoker", barmode="group"
layout = html.Div(
    [
        dcc.RangeSlider(
            id="date-slider",
            min=0,
            max=len(dates) - 1,
            step=1,
            marks=mark_dict,
            #tooltip={"placement": "bottom", "always_visible": True},
        ),
        dcc.Graph(id="bar-chart"),
        html.H5("Note: Change company index to real name..."),
        html.H5("Note: Point out each model's position and holding days...")
    ]
)



@callback(Output("bar-chart", "figure"), Input("date-slider", "value"))
def update_bar_chart(value):
    if value == None:
        value = [0,len(dates)-1]
    start = dates[value[0]]
    end = dates[value[1]]
    updated_fig = generate_bar(start,end)
    return updated_fig

