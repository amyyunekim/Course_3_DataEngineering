
import pandas as pd
import numpy as np
import datetime
import geopandas
from shapely import wkt

def clean_dates(df):
    df['date']=pd.to_datetime(df['date'])
    df['year']=pd.DatetimeIndex(df['date']).year
    df['month']=pd.DatetimeIndex(df['date']).month
    return df

def clean_geo(df):
    df['center_point'] = geopandas.GeoSeries.from_wkt(df['center_point'])
    gdf = geopandas.GeoDataFrame(df,geometry='center_point')
    gdf['lon'] = gdf['center_point'].x
    gdf['lat'] = gdf['center_point'].y
    return gdf


