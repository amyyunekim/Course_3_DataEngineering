
from import_BigQuery import get_data #should this step be included in the pipeline?
from store_sqlite import write_to_sqlite
from create_df import create_df
from clean import *
from summaries import *
#from write_to_csv import write_to_csv


#def get_data():
#    query = '''
#        SELECT *
#        FROM table
#    '''
#    
#    data = conn.execute(query)
#    return data

def run_pipeline():
    write_to_sqlite()
    df=create_df()
    df=clean_dates(df)
    gdf= clean_geo(df)

    ## write summaries
    center_point_summary(gdf)
    zipcode_summary(gdf)

if __name__ == '__main__':
    run_pipeline()
    # if the name of my python instance is main, then go ahead and run the application. 
    # When you later run Python app.py in the terminal window the instance will be named main so it will run