from grpc import Status
import pandas as pd


def zipcode_summary(gdf):
    summary=gdf.groupby(['zipcode','city','county','year'])['count_lightning'].sum().reset_index()
    return summary

def zipcode_summary_time(gdf):
    graph_data=gdf.groupby(["zipcode","date"])['count_lightning'].sum().reset_index()
    graph_data['zipcode'] = graph_data['zipcode'].astype(str)
    
    totals=pd.DataFrame(graph_data.groupby(['date'])['count_lightning'].sum().reset_index())
    totals.insert(0,'zipcode','Total')
    
    graph_data=graph_data.append(totals,ignore_index=True)
    return graph_data

def yearly_stats(summary): #yearly stats
    stats1=(summary
        .groupby(['zipcode','city','county'])['count_lightning']
        .agg(['mean','std','min','max'])
        .sort_values(['mean'], ascending = False)
        .reset_index())
    stats1['rank'] =stats1['mean'].rank(ascending=False).astype(int)
    return stats1

def overall_stats(summary2):
    stats2=pd.DataFrame((summary2['count_lightning']
            .agg(['mean','std','min','max'])).reset_index())
    return stats2