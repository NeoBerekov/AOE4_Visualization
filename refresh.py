import data_process as dp
import importlib
import altair as alt
import IPython
import pandas as pd
import charts




def refresh_data(rank = None):
    solodata = dp.SoloData(refresh=False)
    charts_list = {}
    if rank is None:
        solodata.refresh_all()
        for df in solodata.ranks_pd:
            charts_list[df] = charts.draw_chart(solodata.ranks_pd[df], df)
        # 导出为json文件
        for df in charts_list:
            charts_list[df].save('charts_' + df + '.json')
    else:
        solodata.refresh_rank(rank)
        charts_list[rank] = charts.draw_chart(solodata.ranks_pd[rank], rank)
        # 导出为json文件
        charts_list[rank].save('charts_' + rank + '.json')
