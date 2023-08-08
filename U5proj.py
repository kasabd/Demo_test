
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import socket
#host=socket.gethostname()
#port=50007

app = Dash(__name__)

server=app.server
app.layout = html.Div([
    html.H4('Regional Under Five Mortality Trend'),
    html.P("Select Region:"),
    
    dcc.Dropdown(
        id="time-series-x-ticker",
        options=["Oromiya", "Amhara","Tigray","Somali","Southern Nations ","Afar","Gambela","Benishangul Gumuz","Harari","Dire Dawa","Addis Ababa"],
        value="Oromiya",
        clearable=False,
    ),
    dcc.Graph(id="time-series-x-time-series-chart"),
])


@app.callback(
    Output("time-series-x-time-series-chart", "figure"), 
    Input("time-series-x-ticker", "value"))
def display_time_series(ticker):
    df1 =pd.read_csv('Regionaltrend.csv') # replace with your own data source
    fig = px.line(df1, x='Year', y=ticker)
    return fig


if __name__ == "__main__":
    app.run_server(port = 9079, debug=True)