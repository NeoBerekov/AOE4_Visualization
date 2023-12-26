import data_process as dp
import charts




def refresh_data(rank = None):
    # If rank is not given, refresh all data
    # If rank is given, refresh the data of given rank
    solodata = dp.SoloData(refresh=False)
    rank_charts = {}
    games_count_charts = {}
    if rank is None:
        solodata.refresh_all()
        for df in solodata.ranks_pd:
            rank_charts[df] = charts.draw_rank_chart(solodata.ranks_pd[df], df)
            games_count_charts[df] = charts.draw_games_count_chart(solodata.ranks_pd[df], df)
        # 导出为json文件
        for df in rank_charts:
            rank_charts[df].save('rank_charts/rank_charts_' + df + '.json')     # Save the charts as json file
        for df in games_count_charts:
            games_count_charts[df].save('games_count_charts/games_count_charts_' + df + '.json')
    else:
        solodata.refresh_rank(rank)
        rank_charts[rank] = charts.draw_rank_chart(solodata.ranks_pd[rank], rank)
        games_count_charts[rank] = charts.draw_games_count_chart(solodata.ranks_pd[rank], rank)
        # 导出为json文件
        rank_charts[rank].save('rank_charts/rank_charts_' + rank + '.json')
        games_count_charts[rank].save('games_count_charts/games_count_charts_' + rank + '.json')

