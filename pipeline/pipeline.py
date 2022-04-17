
from store_sqlite import write_to_sqlite
from create_df import create_df
from clean import *
from summaries import *
from write_to_csv import write_to_csv


def run_pipeline():

    ## get and clean data
    df=create_df()
    df=clean_dates(df)
    gdf= clean_geo(df)

    ## write summaries
    summary=zipcode_summary(gdf)
    graph_data=zipcode_summary_time(gdf)
    stats1=yearly_stats(summary)
    stats2=overall_stats(summary)


    ##output to csv
    summary.to_csv('zipcode_summary.csv', index=False)
    graph_data.to_csv('zipcode_summary_time.csv', index=False)
    stats1.to_csv('stats1.csv', index=False)
    stats2.to_csv('stats2.csv',index=False)

if __name__ == '__main__':
    run_pipeline()
    # if the name of my python instance is main, then go ahead and run the application. 
    # When you later run Python app.py in the terminal window the instance will be named main so it will run

    