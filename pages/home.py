from dash import dcc, register_page
import dash_mantine_components as dmc

register_page(__name__, path="/", icon="fa-solid:home")

import dash
import dash_core_components as dcc

import dash_html_components as html
import plotly.graph_objects as go
import dash_daq as daq
import dash_table
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
from event import get_event

def min_max(x):
    return (x - x.min())/(x.max() - x.min())

#portfolio value data
df = pd.read_csv('./data/project_data/with_simi__action_un_aleatoric_pi2_64_vf2_64_10runs.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df = df.iloc[:,0]#!!之後改，僅選一條序列
portfolio_color = 'green' if (df.iloc[-1]/df.iloc[-2])>0 else 'red'

#uncertainty data
un_df = pd.read_csv("./data/project_data/local_agent_data.csv")
un_df['date'] = pd.to_datetime(un_df['date'])
un_df = un_df.set_index('date')
columns = ['{}_un_epistemic'.format(i) for i in range(int(len(un_df.columns)/3))]
columns1 = ['{}_un_aleatoric'.format(i) for i in range(int(len(un_df.columns)/3))]
un_df_epis = un_df[columns].mean(axis = 1)
un_df_alea = un_df[columns1].mean(axis = 1)
un_df_alea = min_max(un_df_alea)
un_df_epis = min_max(un_df_epis)

#Organize event and warning
event_loader = get_event(un_df_alea,un_df_epis,df)
events = event_loader.get_all_events()
def create_warning(events):
    warning_list = []
    for i in events:
        if 'loss' in i:
            warning_list.append(dmc.Alert(i, title="Warning!", color="red",radius = '15px',style ={'margin':'2px'}))
        elif 'Un' in i:
            warning_list.append(dmc.Alert(i, title="Warning!", color="yellow",radius = '15px',style ={'margin':'2px'}))
    return warning_list

#Trading signal (之後用import 的方式)
trade_df = pd.read_csv("./data/project_data/local_agent_data.csv")
trade_df['date'] = pd.to_datetime(trade_df['date'])
trade_df = trade_df.set_index('date')
columns = ['{}_action'.format(i) for i in range(int(len(trade_df.columns)/3))]
trade_df = trade_df[columns]
trade_tmp = trade_df.iloc[-7:,:]

values = trade_tmp[trade_tmp==1].isna().sum()# how many 0 times
values = values.to_frame()
values.columns = ['Selling']
values['Buying'] = trade_df.shape[0] - values['Selling']
market_trend = 'Bear' if values.mean()['Buying']> values.mean()['Selling'] else 'Bull'
market_color = 'green' if market_trend =='Bear' else "red"

#indicators
indi = pd.read_csv("./data/project_data/indicators_pi2_64_vf2_64_10runs.csv").T
indi.columns = indi.iloc[0,:]
indi = indi.iloc[1:]

# Define the sizes of the main blocks
primary_block_width = "auto"#"450px"
primary_block_height = "350px"
second_block_height = "330px" #this is for second stage elements
message = "Something happened! You made a mistake and there is no going back!"


grid_sizes = {
    "block1": {"column": "3 / span 1", "row": "1 / span 1"},
    "block2": {"column": "2 / span 1", "row": "1 / span 1"},
    "block3": {"column": "1 / span 1", "row": "1 / span 1"},
    "block4": {"column": "1 / span 2", "row": "2 / span 1"},
    "block5": {"column": "3 / span 1", "row": "2 / span 1"}
}

# Define the layout of the dashboard
layout = html.Div(
    style={"display": "grid", "grid-template-columns": "1fr 1fr 1fr", "grid-template-rows": "1fr 1fr", "grid-gap": "10px","width":'auto'},
    children=[
        html.Div(
            style={"padding": "20px","grid-column": grid_sizes["block1"]["column"], "grid-row": grid_sizes["block1"]["row"],
                   "width": primary_block_width, "height": primary_block_height,
                   "border-radius": "15px"},
            children=[
                daq.Gauge(
                    id="figure2-gauge",
                    showCurrentValue=True,
                    units='%',
                    value=un_df_alea.values[-1]*100,
                    max=100,
                    min=0,
                    label="Aleatoric Uncertainty",
                    style={'display': 'block'},
                    #color={"default": "#0000ff"},
                )
            ]
        ),
        html.Div(
            style={ "padding": "20px","grid-column": grid_sizes["block2"]["column"], "grid-row": grid_sizes["block2"]["row"],
                   "width": primary_block_width, "height": primary_block_height,
                   "border-radius": "15px"},
            children=[
                daq.Gauge(
                    id="figure1-gauge",
                    showCurrentValue=True,
                    units='%',
                    value=un_df_epis.values[-1]*100,
                    max=100,
                    min=0,
                    label="Epistemic Uncertainty",
                    style={'display': 'block'},
                    #color={"default": "#0000ff"},
                )
            ]
        ),
        html.Div(
            style={ "padding": "0px","grid-column": grid_sizes["block3"]["column"], "grid-row": grid_sizes["block3"]["row"],
                   "width": primary_block_width, "height": primary_block_height,
                   "border-radius": "15px","block-size": "fit-content"},
            children=[
                html.Div(
                    style={"display": "grid", "grid-template-columns": "1fr 1fr 1fr", "grid-template-rows": "1fr 1fr",
                           "grid-gap": "20px"},
                    children=[
                        html.Div(className="value-block",
                                 style={"border-radius": "15px","padding": "5px"},
                                 children=[
                                     html.H2("Return"),
                                     html.H3("{} %".format(int(df.values[-1])/1000000),style={"color": portfolio_color}),
                                    # dmc.ThemeIcon(
                                    # DashIconify(icon="mdi:arrow-up-bold", width=30,color = 'red', rotate=2, flip="vertical"),
                                    # variant="subtle",
                                    # color = 'red'),
                                 ]
                        ),
                        html.Div(className="value-block",
                                 style={"border-radius": "15px","padding": "5px"},
                                 children=[
                                     html.H2("Year Sharpe Ratio"),
                                     html.H3("{}".format(indi['sharpe_ratio'].values[0]))
                                 ]),
                        html.Div(className="value-block",
                                 style={"border-radius": "15px", "padding": "5px"},
                                 children=[
                                     html.H4("Max Draw Down(%)"),
                                     html.H3("{}".format(indi['max_dropdown'].values[0]*100))#!!
                                 ]),
                        html.Div(className="value-block",
                                 style={"border-radius": "15px","padding": "5px"},
                                 children=[
                                     html.H2("Stock Number"),
                                     html.H3("10")
                                 ]),
                        html.Div(className="value-block",
                                 style={"border-radius": "15px","padding": "5px"},
                                 children=[
                                     html.H2("Decision Trend(Local)"),
                                     html.H3("{}".format(market_trend),style={"color": market_color})
                                 ]),
                        html.Div(className="value-block",
                                 style={"border-radius": "15px","padding": "5px"},
                                 children=[
                                     html.H4("Avg holding days(Local)"),
                                     html.H3("{}".format(47))
                                 ]),
                    ]
                )
            ]
        ),
        html.Div(
            style={ "padding": "20px","grid-column": grid_sizes["block4"]["column"], "grid-row": grid_sizes["block4"]["row"],
                   "width": primary_block_width,
                    "height": primary_block_height,"border-radius": "15px"},
            children=[
                html.Div(
                    children=[
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Scatter(
                                        x=df.index,
                                        y=df.values,
                                        mode='lines',
                                        name='Trend'
                                    )
                                ],
                                layout=go.Layout(
                                    title="Accumulative Portfolio value",
                                    xaxis=dict(title="Date"),
                                    yaxis=dict(title="Portfolio value"),
                                    margin=dict(t=30, r=0, b=30, l=0),
                                    hovermode='x',
                                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                                )
                            ),
                            style={"border-radius": "15px", "height": second_block_height,#"width": primary_block_width,
                            }
                        )
                    ]
                )
            ]
        ),
        html.Div(
            style={"padding": "20px","grid-column": grid_sizes["block5"]["column"], "grid-row": grid_sizes["block5"]["row"],
                   "width": primary_block_width, "height": primary_block_height,
                   "border-radius": "15px","overflow": "scroll"},
            children=create_warning(events)
        )
    ]
)
