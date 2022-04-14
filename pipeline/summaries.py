import pandas as pd

def center_point_summary(gdf):
    summary1=gdf.groupby(['lat','lon','zipcode','date',])['count_lightning'].sum().reset_index()
    return summary1

def zipcode_summary(gdf):
    summary2=gdf.groupby(["zipcode","year"])['count_lightning'].sum().reset_index()
    return summary2

def zipcode_summary_time(gdf):
    summary3=gdf.groupby(["zipcode","date"])['count_lightning'].sum().reset_index()
    return summary3
