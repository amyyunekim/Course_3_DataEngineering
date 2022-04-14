### cleaning.py
def remove_weird_characters(text):
    return text

def clean(text):
    remove_weird_characters(text)
    return data
    
### aggregating.py
def aggregate_date():
    return data

### summary_stats.py
def get_summary_stats():
    return data

### writing.py
def write_data():
    #write to SQL database or create CSV file

### pipeline.py
from cleaning import clean
from aggregating import aggregate_date
from summary_stats import get_summary_stats
from writing import write_data
import SQLAlchemy

def get_data():
    query = '''
        SELECT *
        FROM table
    '''
    
    data = conn.execute(query)
    return data

def run_pipeline():
    data = get_data()
    cleaned_data = clean_data(data)
    aggregated_data = aggregate_data(cleaned_data)
    summary_data = get_summary_stats(summary_data)
    write_data(writing)

if name == '__main__':
    run_pipeline()
    # if the name of my python instance is main, then go ahead and run the application. 
    # When you later run Python app.py in the terminal window the instance will be named main so it will run