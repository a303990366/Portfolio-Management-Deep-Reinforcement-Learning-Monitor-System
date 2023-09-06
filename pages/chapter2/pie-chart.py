from dash import dcc, html, Input, Output, callback, register_page
import dash
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
register_page(__name__, icon="fa:pie-chart")

#load data
df = pd.read_csv(r"./data/project_data/decision.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
dates = list(df.index)

#create slider mark
mark_dict = {}
for i in [int(i * (df.shape[0]-1)/5) for i in range(0,6)]:
    mark_dict[i] = datetime.strftime(df.index[i],'%Y-%m-%d')


def generate_pie_chart(start,end):
    values = df[start:end].mean().round(2)
    labels = list(df.columns)
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6)])
    return fig

layout = html.Div(
    [
        dmc.Text("Asset ratio:"),
        dcc.RangeSlider(
            id="date-slider",
            min=0,
            max=len(dates) - 1,
            step=1,
            marks=mark_dict,
            #tooltip={"placement": "bottom", "always_visible": True},
        ),
        dmc.Space(h=20),
        dcc.Graph(id="pie-chart", figure=generate_pie_chart(dates[0],dates[-1])),
        html.H5("Note: Change company index to real name.."),
        html.H5("Note: Add a barplot for showing company categories")
    ]
)


@callback(
    dash.dependencies.Output("pie-chart", "figure"),
    [dash.dependencies.Input("date-slider", "value")]
)
def update_pie_chart(value):
    if value is None:
        value = [0, len(dates)-1]
    start = dates[value[0]]
    end = dates[value[1]]
    updated_fig = generate_pie_chart(start,end)
    return updated_fig

