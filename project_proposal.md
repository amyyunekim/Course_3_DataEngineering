
## Question/Need:

What is the question behind your analysis or model and what practical impact will your work have?

- Understanding patterns in lightning strikes in the US.
    - Where are lightning strikes occurring the most/least?
    - Which days of the years have the highest amount of lightning per area?

Who is your client and how will that client benefits from exploring this question or building this model/system?

- Emergency services, electrical companies, insurance companies

What does your end-to-end data pipeline look like? 

![pipeline_diagram](./images/pipeline_diagram.png)

1. <b>Data Ingestion:</b>
    Use BigQuery API to access the public dataset. 
    Only 1TB/month of querying is allowed within the Google Free Tier as a constraint.

2. <b> Data Storage:</b>
Data will be housed in SQL Lite as it is tabular data

3. <b> Processing: </b> 
Data will be brought into Python using SQL Alchemy and aggregated using pandas to compute key statistics to build visualizations. If time permits, some of these may be rebuilt in Spark.

4. <b> Deployment: </b> 
Use Streamlit which will take user inputs and display the requested summary information.

Testing: 
- Make sure data ingestion is robust against erroneous data. Build data quality checks - Are datapoints correct and fall within an expected range?
- Is web app stable? Have users try to break it & potentially build in error handling.


## Data Description:

What dataset(s) do you plan to use, and how will you obtain the data? Please include a link! (The link can be to the dataset you’re downloading, the site you’re scraping, etc.)

- Big Query public data:
https://console.cloud.google.com/marketplace/product/noaa-public/lightning?project=data-engineering-345807 

What is an individual sample/unit of analysis in this project? In other words, what does one row or observation of the data represent?
-  number of lightning strikes in a 11km grid on one day

Do you plan to be able to automatically pull in new data at a regular cadence (e.g. with Airflow or a cron job)?
- the BigQuery dataset refreshes every day so potentially refresh the project dataset every day too with a CRON job, depending on time.

What characteristics/features do you expect to work with? In other words, what are your columns of interest?
- one row will have the following columns: time-stamp, zipcode, city, state, center_point (for mapping)


## Tools:

How do you intend to meet the tools requirement of the project?
- Data ingestion: Big Query API
- Data storage: SQL Lite
- Processing: SQL Alchemy, Pandas
- Deployment: Streamlit

## MVP Goal:

Have data ingestion, data storage and initial pandas processing complete.