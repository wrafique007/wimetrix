import chart_studio.plotly as py
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

df = pd.read_csv('image_content.csv', sep=',')

print(df)

layout = go.Layout(
    autosize=False,
    width=2000,
    height=2000,
    xaxis=go.layout.XAxis(linecolor="black", linewidth=1, mirror=True),
    yaxis=go.layout.YAxis(linecolor="black", linewidth=1, mirror=True),
    margin=go.layout.Margin(l=75, r=75, b=125, t=125, pad=4),
)

column_widths = [150, 50, 150, 50, 50, 50, 50, 50, 50,
                 50, 50, 50, 150, 150, 50, 50, 50, 50]

#layout = dict(autosize=True)
image_content = FF.create_table(df, height_constant=30, index=False, )
fig = go.Figure(data=image_content, layout=layout)
fig.layout.width = 3200

f2 = go.FigureWidget(fig)
f2.show()
#fig.show()
#iplot(fig)
#py.iplot(image_content, filename='image_content-table')
""" fig = go.Figure(data=[go.Table(
    columnwidth=column_widths,
    header=dict(values = df.columns), 
    cells=dict(values=df.iloc[0:]))
])
fig.show()  """
