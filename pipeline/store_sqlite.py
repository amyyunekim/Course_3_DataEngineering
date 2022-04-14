from sqlalchemy import create_engine
import db_dtypes 
import pandas as pd


def write_to_sqlite():

    df=pd.read_csv('/lightning_CA.csv')

    engine = create_engine('sqlite:///lightning.db', echo=True)
    sqlite_connection = engine.connect()
    sqlite_table = "lightning_CA"
    df.to_sql(sqlite_table,sqlite_connection,if_exists='replace')
