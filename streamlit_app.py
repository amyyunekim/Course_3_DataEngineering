"""
Streamlit Housing App Demo
    
Make sure to install Streamlit with `pip install streamlit`.

Run `streamlit hello` to get started!

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

# load data ####################################################

@st.cache(allow_output_mutation=True)

def load_data(path):
    df = pd.read_csv(path)
    return df

center_point_summary=load_data('pipeline/center_point_summary.csv')
center_point_summary['date']=pd.to_datetime(center_point_summary['date'])

zipcode_summary = load_data('pipeline/zipcode_summary.csv')
zipcode_summary['zipcode'] = zipcode_summary['zipcode'].astype(str)
zipcode_summary_2020 = zipcode_summary.loc[zipcode_summary["year"] == 2020]

#load geojson
with open("CA_small.geojson") as response:
    geo = json.load(response)


# Summary table ################################################

st.write(
'''
## California Lightning Data
Summary of lightning strikes by 11km grid centerpoint

''')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(center_point_summary)

# map ##########################################################

# slider map

st.write(
'''
## California Map

''')

year_to_filter = st.slider('year', 1987, 2020, 2020) 
filtered_data = center_point_summary[center_point_summary['date'].dt.year == year_to_filter]
st.subheader(f'Map of all lightning strikes in {year_to_filter}')
st.map(filtered_data)

# chloropeth map 

#https://github.com/ozgunhaznedar/swiss_renewable_energy_app/blob/main/src/main.py

st.write(
'''
## Lightning strikes in 2020 by zipcode

''')

fig = go.Figure(
    go.Choroplethmapbox(
        geojson=geo,
        locations=zipcode_summary_2020.zipcode,
        featureidkey='properties.ZCTA5CE10',
        z=zipcode_summary_2020.count_lightning,
        colorscale="sunsetdark",
        marker_opacity=0.5,
        marker_line_width=0,
    ))
fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=5,
    mapbox_center={"lat": 37.7518, "lon": -119.6318},
    width=800,
    height=600,
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

st.plotly_chart(fig)

