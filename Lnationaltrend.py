import pandas as pd
import numpy as np
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input,Output
from dash import callback_context


load_figure_template('LUX')


###--------------Build the figures / dropdowns------------------------------------

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10.5rem",
    "padding": "2rem 2rem",
    "background-color": "#f8f9fa",
    #"background-color": "#5072A7",
}


sidebar = html.Div(
    [
        html.H6("National Under Five Mortality Trend"),
        html.Hr(),
        html.P(
            "Select Mortality Type ", className="lead"
    

        ),
        dbc.Nav(
            [
                dcc.Dropdown(
                id="time-series-x-ticker",
                options=["Neonatal","Infant","Under Five"],
                value="Neonatal",
                clearable=False,
        
                ),
                #dcc.Graph(id="time-series-x-time-series-chart"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


###---------------Create the layout of the app ------------------------

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
server=app.server
app.layout = html.Div(children = [
                dbc.Row([
                    dbc.Col(),

                    dbc.Col(html.H4('National Child Mortality Projection'),width = 9, style = {'margin-left':'7px','margin-top':'7px'})
                    ]),
                dbc.Row(
                    [dbc.Col(sidebar),
                    dbc.Col(dcc.Graph(id = 'time-series-x-time-series-chart'), width = 10, style = {'margin-left':'14px', 'margin-top':'7px', 'margin-right':'14px'})
                    ])
    ]
)

@app.callback(
    Output("time-series-x-time-series-chart", "figure"), 
    Input("time-series-x-ticker", "value"))
def display_time_series(ticker):
    df =pd.read_csv('NationalChildMortalityTrend.csv') # replace with your own data source
    fig = px.line(df, x='Year', y=ticker)
    return fig


if __name__ == "__main__":
    #app.run_server(debug=True)
    app.run_server(port = 9023, debug=True)