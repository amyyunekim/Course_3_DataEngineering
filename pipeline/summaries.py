import pandas as pd

def center_point_summary(gdf):
    center_point_summary=gdf.groupby(['lat','lon','zipcode','date',])['count_lightning'].sum().reset_index()
    center_point_summary.to_csv('center_point_summary.csv', index=False)
    return 

def zipcode_summary(gdf):
    zipcode_summary=gdf.groupby(["zipcode","year"])['count_lightning'].sum().reset_index()
    zipcode_summary.to_csv('zipcode_summary.csv', index=False)
    return zipcode_summary
