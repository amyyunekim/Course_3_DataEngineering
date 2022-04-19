"""
To run this app:

1. cd into this directory
2. Run `streamlit run streamlit_app.py`
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import datetime
import numpy as np
import json
import plotly.graph_objects as go

from utils import chart


# formatting ###################################################

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


# load data ####################################################

@st.cache(allow_output_mutation=True)
def load_data(path):
    df = pd.read_csv(path)
    return df

zipcode_summary = load_data('pipeline/zipcode_summary.csv')
zipcode_summary['zipcode'] = zipcode_summary['zipcode'].astype(str)

zipcode_summary_time=load_data('pipeline/zipcode_summary_time.csv')
zipcode_summary_time['date']=pd.to_datetime(zipcode_summary_time['date'])
zipcode_summary_time['zipcode'] = zipcode_summary_time['zipcode'].astype(str)

stats1=load_data('pipeline/stats1.csv')
stats2=load_data('pipeline/stats2.csv')

#load geojson
with open("ca_california_zip_codes_geo_v2.min.json") as response:
    geo = json.load(response)


# title ##########################################################

st.write(
'''
## California Lightning Data

''')

# map ##########################################################

# chloropeth map 

#https://github.com/ozgunhaznedar/swiss_renewable_energy_app/blob/main/src/main.py

st.subheader('Yearly lightning strikes by zipcode')

year_to_filter = st.slider('year', 1987, 2020, 2020) 
filtered_data = zipcode_summary[zipcode_summary['year'] == year_to_filter]

fig = go.Figure(
    go.Choroplethmapbox(
        geojson=geo,
        locations=filtered_data.zipcode,
        featureidkey='properties.ZCTA5CE10',
        z=filtered_data.count_lightning,
        colorscale="sunsetdark",
        marker_opacity=0.6,
        marker_line_width=0,
    ))


fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_zoom=5,
    mapbox_center={"lat": 37.7518, "lon": -119.6318},
    width=800,
    height=600,
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

st.plotly_chart(fig)

# Stats################################################
mean = stats2['count_lightning'][0]
std  = stats2['count_lightning'][1]
max  = stats2['count_lightning'][3]

#if st.checkbox('Show extra stats '):

st.subheader('Yearly lightning strike statistics')
st.write(f'Mean: {mean}')
st.write(f'Standard Deviation: {std}')
st.write(f'Max: {max}')
st.write(stats1[['rank','zipcode','county','mean','std','min','max']])
    

space(1)

# Line graph 

#https://share.streamlit.io/streamlit/example-app-commenting/main

st.subheader("Daily lightning strikes from 1987 to 2020")

source = zipcode_summary_time
all_zipcodes = source.zipcode.unique()
zipcodes = st.multiselect("Choose zipcode or 'Total' to visualize", all_zipcodes, all_zipcodes[:3])

space(1)

source = source[source.zipcode.isin(zipcodes)]
chart = chart.get_chart(source)
st.altair_chart(chart, use_container_width=True)

space(2)



