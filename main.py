import data_process as dp
import importlib
import altair as alt
import IPython
import pandas as pd
import charts

#always fail to sync with the latest version, so I have to reload it manually
solodata = dp.SoloData(refresh=False)
charts_list = {}
for df in solodata.ranks_pd:
    charts_list[df] = charts.draw_chart(solodata.ranks_pd[df],df)
#导出为html文件
for df in charts_list:
    charts_list[df].save('charts_'+df+'.json')
