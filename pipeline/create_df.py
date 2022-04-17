from sqlalchemy import create_engine
import pandas as pd

def create_df():
    engine= create_engine('sqlite:///lightning.db')
    df=pd.read_sql(
    '''
    SELECT date, 
    zipcode, 
    city, 
    county,
    state_name as state, 
    number_of_strikes as count_lightning, 
    center_point_geom as center_point
    FROM lightning_CA

    '''
    ,engine)

    return df
