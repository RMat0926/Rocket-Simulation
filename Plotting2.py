import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

dfK = pd.read_csv("Infocambio_cinematico.csv")
dfD = pd.read_csv("Infocambio_dinamico.csv")
fig = make_subplots(rows=2, cols=2, start_cell="top-left", subplot_titles=("Acceleration Y", "Speed Y", "Height", "Air Drag"))

accelerationY = go.Scatter(x = dfK['Seconds'], y = dfK[' Acceleration Y'])
speedYGeneral = go.Scatter(x = dfK['Seconds'], y = dfK[' Speed Y'])
height = go.Scatter(x=dfK['Seconds'], y = dfK[' Height'])
drag = go.Scatter(x = dfD['Seconds'], y = dfD[' Air Resistance'] )

fig.add_trace(accelerationY, row = 1, col = 1)
fig.add_trace(height, row = 2, col = 1 )
fig.add_trace(speedYGeneral, row = 1, col = 2)
fig.add_trace(drag, row = 2, col = 2)

fig.update_xaxes(title_text="Time (s)", row=2, col=1)
fig.update_xaxes(title_text="Time (s)", row=2, col=2)
fig.update_xaxes(title_text="Time (s)", row=1, col=1)
fig.update_xaxes(title_text="Time (s)", row=1, col=2)
fig.update_yaxes(title_text="Acceleration Y (m/s^2)", row=1, col=1)
fig.update_yaxes(title_text="Speed Y (m/s)", row=1, col=2)
fig.update_yaxes(title_text="Height (m)", row=2, col=1)
fig.update_yaxes(title_text="Air Drag (N)", row=2, col=2)

fig.update_layout(height=1000, width=1400, title_text="Rocket Simulation Data")
fig.show()