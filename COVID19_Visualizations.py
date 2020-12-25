#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:41:14 2020

@author: yiannimercer
"""


# Import libraries
import numpy as np 
import pandas as pd 
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
# Displaying plots while in Spyder
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

# Read Data
df = pd.read_csv("covid_19_data.csv")

# Rename columns
df = df.rename(columns={'Country/Region':'Country'})
df = df.rename(columns={'ObservationDate':'Date'})

# Manipulate Dataframe
df_countries = df.groupby(['Country', 'Date']).sum().reset_index().sort_values('Date', ascending=False)
df_countries = df_countries.drop_duplicates(subset = ['Country'])
df_countries = df_countries[df_countries['Confirmed']>0]
df_countries

# Create the Choropleth
fig_static = go.Figure(data=go.Choropleth(
    locations = df_countries['Country'],
    locationmode = 'country names',
    z = df_countries['Confirmed'],
    colorscale = 'Reds',
    marker_line_color = 'black',
    marker_line_width = 0.5,
))
fig_static.update_layout(
    title_text = 'Confirmed COVID-19 Cases as of November 15, 2020',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = True,
        projection_type = 'equirectangular'
    )
)
# Will open Google Chrome and will display the plot
plot(fig_static)

# Create the Choropleth animated map

# Manipulating the original dataframe
df_countrydate = df[df['Confirmed']>0]
df_countrydate = df_countrydate.groupby(['Date','Country']).sum().reset_index()
df_countrydate


# Creating Visualization 
fig_vis = px.choropleth(df_countrydate,
                    locations = 'Country',
                    locationmode = 'country names',
                    color = 'Confirmed',
                    hover_name = 'Country',
                    animation_frame = 'Date')

fig_vis.update_layout(
    title_text = 'Global Spread of COVID19 (up to 11/15/2020)',
    title_x = 0.5,
    geo = dict(
        showframe = False,
        showcoastlines = True,
        ))
plot(fig_vis)
    

