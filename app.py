import dash
from dash import dcc, html, Output, Input, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash_auth
VALID_USERNAME_PASSWORD_PAIRS = {
    '0001': '0001'
}
templates = ["darkly"]
load_figure_template(templates)

background_color = '#222222'
header_color = '#375a7f'

app = dash.Dash(__name__, use_pages=True,assets_url_path="assets",external_stylesheets=[dbc.themes.DARKLY])

auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

def create_nav_link(icon, label, href):
    return dcc.Link(
        dmc.Group(
            [
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=30,
                    radius=30,
                    variant="light",
                    color = background_color
                ),
                #dmc.Text(label, size="lg", color="white"),
                html.H5(label, style= {'color' : "white"}),
            ]
        ),
        href=href,
        style={"textDecoration": "none"},
    )


sidebar = dmc.Navbar(
    fixed=True,
    width={"base": 300},
    position={"top": 80},
    height=300,
    style={'background-color':background_color},
    children=[
        dmc.ScrollArea(
            offsetScrollbars=True,
            type="scroll",
            children=[
                dmc.Stack(
                    children=[
                        create_nav_link(
                            icon="radix-icons:rocket",
                            label="Home",
                            href="/",
                        ),
                    ],
                ),
                # dmc.Divider(
                #     label="Local Agents", style={"marginBottom": 20, "marginTop": 20}
                # ),
                html.H5("Local Agents", style={"marginBottom": 20, "marginTop": 20}),
                dmc.Stack(
                    children=[
                        create_nav_link(
                            icon=page["icon"], label=page["name"], href=page["path"]
                        )
                        for page in dash.page_registry.values()
                        if page["path"].startswith("/chapter1")
                    ],
                ),
                # dmc.Divider(
                #     label="Global Agent", style={"marginBottom": 20, "marginTop": 20}
                # ),
                html.H5("Global Agent", style={"marginBottom": 20, "marginTop": 20}),
                dmc.Stack(
                    children=[
                        create_nav_link(
                            icon=page["icon"], label=page["name"], href=page["path"]
                        )
                        for page in dash.page_registry.values()
                        if page["path"].startswith("/chapter2")
                    ],
                ),
            ],
        )
    ]
)

app.layout = dmc.Container(
    children = [
        dmc.Header(
            height=70,
            children=[dmc.Text("Uncertainty-based DRL system",style={"fontSize": 40})],
            #style={'background-color':'black'}
            className="dbc",
            style={'background-color': header_color},
        ),
        sidebar,
        dmc.Container(
            dash.page_container,
            size="lg",
            pt=20,
            style={"marginLeft": 300,"marginRight": 0},
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
