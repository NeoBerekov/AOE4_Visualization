import pandas as pd
import requests
import json
import plotly.express as px
import plotly.graph_objects as go
import data_process as dp
import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
from mpl_toolkits.mplot3d import Axes3D

def init(refresh=False):
    data = dp.SoloData(refresh=refresh)
    return data


# solodata = init()
# # 创建一个2x2的网格
# fig = make_subplots(rows=2, cols=2)
#
# fig.add_trace(
#     go.Bar(
#         x=solodata.ranks_pd['Bronze']['civilization'],
#         y=solodata.ranks_pd['Bronze']['win_rate']-50,
#         marker=dict(
#             color=solodata.ranks_pd['Bronze']['win_rate'],  # set color to an array/list of desired values
#             colorscale=[[0, 'red'],[0.5, 'lightblue'], [1, 'green']],  # define custom colorscale
#             colorbar=dict(title="Win Rate"),  # add colorbar title
#             cmin=solodata.ranks_pd['Bronze']['win_rate'].min(),  # set colorbar min value
#             cmax=solodata.ranks_pd['Bronze']['win_rate'].max(),  # set colorbar max value
#             showscale=False,
#             opacity=0.8
#         ),
#         showlegend=False
#     ),
#     row=1, col=1
# )
#
# # 为第一个子图添加图片
# for i, x_value in enumerate(solodata.ranks_pd['Bronze']['civilization']):
#     fig.add_layout_image(
#         dict(
#             source=f"images/{x_value}.png",  # replace with the URL of your image
#             xref="x1",
#             yref="y1",
#             x=x_value,
#             y=solodata.ranks_pd['Bronze']['win_rate'][i],
#             sizex=20,
#             sizey=20,
#             xanchor="center",
#             yanchor="bottom"
#         )
#     )
#
# fig.add_trace(
#     go.Bar(
#         x=solodata.ranks_pd['Silver']['civilization'],
#         y=solodata.ranks_pd['Silver']['win_rate']-50,
#         marker=dict(
#             color=solodata.ranks_pd['Silver']['win_rate'],  # set color to an array/list of desired values
#             colorscale=[[0, 'red'], [0.5, 'lightblue'], [1, 'green']],  # define custom colorscale
#             colorbar=dict(title="Win Rate"),  # add colorbar title
#             cmin=solodata.ranks_pd['Silver']['win_rate'].min(),  # set colorbar min value
#             cmax=solodata.ranks_pd['Silver']['win_rate'].max(),  # set colorbar max value
#             showscale=False,
#             opacity=0.8
#         ),
#         showlegend=False
#     ),
#     row=2, col=2
# )
#
# # 为第二个子图添加图片
# for i, x_value in enumerate(solodata.ranks_pd['Silver']['civilization']):
#     fig.add_layout_image(
#         dict(
#             source=f"images/{x_value}.png",  # replace with the URL of your image
#             xref="x2",
#             yref="y2",
#             x=x_value,
#             y=solodata.ranks_pd['Silver']['win_rate'][i],
#             sizex=0.2,
#             sizey=0.2,
#             xanchor="center",
#             yanchor="bottom"
#         )
#     )
#
# fig.update_yaxes(range=[-10, 10], row=1, col=1)
# fig.update_yaxes(range=[-10, 10], row=2, col=2)
# fig.update_xaxes(showticklabels=False, row=1, col=1)
# fig.update_xaxes(showticklabels=False, row=2, col=2)
# fig.show()
