from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from matplotlib import pyplot
app = Dash(__name__)
server=app.server
app.layout = html.Div([
    html.H4('Regional 2016  estimate  for  Neonatal, infant, U5M'),
    html.P("Select Mortality Type:"),
    dcc.Dropdown(
        id="time-series-x-ticker",
        options=["Neonatal","Infant","U5M"],
        value="Neonatal",
        clearable=False,
    ),
    dcc.Graph(id="time-series-x-time-series-chart"),
    
])

@app.callback(
    Output("time-series-x-time-series-chart", "figure"), 
    Input("time-series-x-ticker", "value"))
def display_time_series(ticker):
    df3=pd.read_csv('Regionalpointestimate.csv')
    #fig = px.line(df3, x='Region', y=ticker)
    fig = px.bar(df3, x='Region', y=ticker,text=ticker)
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=4, uniformtext_mode='hide')
    return fig
if __name__ == "__main__":
    #app.run_server(debug=True)
    app.run_server(port = 9045, debug=True)