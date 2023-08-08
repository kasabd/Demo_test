import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from matplotlib import pyplot

app = Dash(__name__)
server=app.server
app.layout = html.Div([
    html.H4('National Mortality Trend'),
    html.P("Mortality Type:"),
    dcc.Dropdown(
        id="time-series-x-ticker",
        options=["Neonatal","Infant","Under Five"],
        value="Neonatal",
        clearable=False,
    ),
    
    dcc.Graph(id="time-series-x-time-series-chart"),
])

@app.callback(
    Output("time-series-x-time-series-chart", "figure"), 
    Input("time-series-x-ticker", "value"))
def display_time_series(ticker):
    df =pd.read_csv('NationalChildMortalityTrend.csv') # replace with your own data source
    fig = px.line(df, x='Year', y=ticker,markers=True)
    return fig


if __name__ == "__main__":
    #app.run_server(debug=True)
    app.run_server(port = 9011, debug=True)