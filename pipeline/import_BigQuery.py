
import os
import pandas as pd
from google.cloud import bigquery 

##input credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/amykim/Documents/Metis/Course_3_Engineering/App/BigQuery/data-engineering-345807-a02ba30a47dd.json"
client = bigquery.Client()

def get_data():
    QUERY = ('''

    SELECT * FROM `bigquery-public-data.utility_us.zipcode_area` z,`bigquery-public-data.noaa_lightning.lightning_*` l 
        WHERE ST_CONTAINS(ST_GeogFromText(z.zipcode_geom) , l.center_point_geom) and state_name = 'California'
 
    ''')

    query_job = client.query(QUERY)  # API request
    query_result = query_job.result() 
    df= query_result.to_dataframe()
    return df

