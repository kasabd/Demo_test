import plotly.graph_objects as go
#server=app.server
Type = ['Rural', 'Urban']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=Type,
    y=[32.77, 18.24],
    name='Neonatal',
    #marker_color='indianred'
    marker_color='darkblue',

  
))
fig.add_trace(go.Bar(
    x=Type,
    y=[51.23, 30.4],
    name='Infant',
    #marker_color='lightsalmon'
    marker_color= 'royalblue'
))
fig.add_trace(go.Bar(
    x=Type,
    y=[65.54,39.01],
    name='Under Five',
    marker_color='lightsalmon'
))
# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()