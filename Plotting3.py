import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("Infocambio_cinematico.csv")
trajectory = go.Scatter(x=df[' Delta X'], y=df[' Height'])
axis_range = [-9,9]

fig = go.Figure()

fig.update_xaxes(range=axis_range,title = 'y', tickmode = 'linear',
                 showticklabels = True, dtick = 200000, side='top',gridcolor="rgb(224,224,224)")

fig.update_yaxes(range=axis_range,title = 'x', tickmode = 'linear',
                 showticklabels = True, dtick = 200000,  side='right', gridcolor="rgb(224,224,224)")

fig.add_vline(x=0, line_width=3)
fig.add_hline(y=0, line_width=3)

fig.add_trace(trajectory)

fig.update_layout(plot_bgcolor='rgb(255,255,255)', height=800, width=800)

fig.show()
