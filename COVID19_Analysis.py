#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:04:38 2020

@author: yiannimercer
"""

##Load in libs and explore data
import pandas as pd #Data
import numpy as np #Math if we neeed it 
import matplotlib.pyplot as plt #Visualization
import seaborn as sns #Visualization
import datetime as dt #Date column
import plotly.express as px #interactive graphs
import plotly.io as pio #changing the below features
pio.renderers.default='browser' # interactive graphs in plotly.express
pio.renderers.default = "svg" #load in spyder
import geopandas as gpd
import folium #Map



##Daily Dataset

df_daily = pd.read_csv('COVID-19_Daily_Cases__Deaths__and_Hospitalizations.csv')
df_daily['Date'] = pd.to_datetime(df_daily['Date'])

df_daily.info()
df_daily.columns
df_daily.describe()

##Feature Engineering

#Deaths over cases
df_daily['DeathRate'] =df_daily["Deaths - Total"] / df_daily["Cases - Total"]

df_daily['DeathRate'].mean()

##EDA
fig=px.line(df_daily,x="Date",y="Cases - Total",title="Chicago COVID Cases (3/1/2020 - 12/23/2020)",template="plotly_dark")
fig.show()

fig=px.line(df_daily,x="Date",y="Deaths - Total",title="Chicago COVID Deaths (3/1/2020 - 12/23/2020)",template="plotly_dark")
fig.show()

fig=px.line(df_daily,x="Date",y="Hospitalizations - Total",title="Chicago COVID Hospitalizations (3/1/2020 - 12/23/2020)",template="plotly_dark")
fig.show()

fig=px.line(df_daily,x="Date",y="DeathRate",title="Chicago COVID Mortality Rate (3/1/2020 - 12/23/2020)",template="plotly_dark")
fig.show()




cases_age = ['Cases - Age 0-17', 
             'Cases - Age 18-29', 
             'Cases - Age 30-39',
             'Cases - Age 40-49', 
             'Cases - Age 50-59', 
             'Cases - Age 60-69',
             'Cases - Age 70-79', 
             'Cases -  Age 80+', 'Cases - Age Unknown']

cases_gender = ['Cases - Female', 
                'Cases - Male', 
                'Cases - Unknown Gender']

cases_race = ['Cases - Latinx', 
              'Cases - Asian Non-Latinx',
              'Cases - Black Non-Latinx', 
              'Cases - White Non-Latinx',
              'Cases - Other Race Non-Latinx', 
              'Cases - Unknown Race/Ethnicity']

deaths_age = ['Deaths - Age 0-17', 
              'Deaths - Age 18-29', 
              'Deaths - Age 30-39',
              'Deaths - Age 40-49', 
              'Deaths - Age 50-59',
              'Deaths - Age 60-69',
              'Deaths - Age 70-79', 
              'Deaths - Age 80+', 'Deaths - Age Unknown']

deaths_gender = ['Deaths - Female', 
                 'Deaths - Male', 
                 'Deaths - Unknown Gender']

deaths_race = ['Deaths - Latinx',
               'Deaths - Asian Non-Latinx',
               'Deaths - Black Non-Latinx',
               'Deaths - White Non-Latinx',
               'Deaths - Other Race Non-Latinx']

hosp_age  = ['Hospitalizations - Age 0-17', 
             'Hospitalizations - Age 18-29', 
             'Hospitalizations - Age 30-39',
             'Hospitalizations - Age 40-49', 
             'Hospitalizations - Age 50-59', 
             'Hospitalizations - Age 60-69',
             'Hospitalizations - Age 70-79', 
             'Hospitalizations - Age 80+',
             'Hospitalizations - Age Unknown']

hosp_gender = ['Hospitalizations - Female', 
               'Hospitalizations - Male', 
               'Hospitalizations - Unknown Gender']

hosp_race =   ['Hospitalizations - Latinx',
               'Hospitalizations - Asian Non-Latinx',
               'Hospitalizations - Black Non-Latinx',
               'Hospitalizations - White Non-Latinx',
               'Hospitalizations - Other Race Non-Latinx']

df_daily.columns



df_daily[cases_age].sum().plot.pie(shadow = True, legend=False,
                                   figsize=(15,10), autopct='%1.1f%%',title = 'Chicago COVID19 Cases by Age Group')


df_daily[cases_gender].sum().plot.pie(shadow = True, legend=False,
                                   figsize=(15,10), autopct='%1.1f%%',title = 'Chicago COVID19 Cases by Gender')

df_daily[cases_race].sum().plot.pie(shadow = True, legend=False,
                                   figsize=(15,10), autopct='%1.1f%%',title = 'Chicago COVID19 Cases by Race/Ethnicity')


df_daily[deaths_age].sum().plot.pie(shadow = True, legend=False,
                                   figsize=(15,10), autopct='%1.1f%%',title = 'Chicago COVID19 Deaths by Age Group')


df_daily[deaths_gender].sum().plot.pie(shadow = True, legend=False,
                                   figsize=(15,10), autopct='%1.1f%%',title = 'Chicago COVID19 Deaths by Gender')

df_daily[deaths_race].sum().plot.pie(shadow = True, legend=False,
                                   figsize=(15,10), autopct='%1.1f%%',title = 'Chicago COVID19 Deaths by Race/Ethnicity')

df_daily[hosp_age].sum().plot.pie(shadow = True, legend=False,
                                   figsize=(15,10), autopct='%1.1f%%',title = 'Chicago COVID19 Hospitilizations by Age Group')

df_daily[hosp_gender].sum().plot.pie(shadow = True, legend=False,
                                   figsize=(15,10), autopct='%1.1f%%',title = 'Chicago COVID19 Hospitilizations by Gender')


df_daily[hosp_race].sum().plot.pie(shadow = True, legend=False,
                                   figsize=(15,10), autopct='%1.1f%%',title = 'Chicago COVID19 Hospitilizations by Race/Ethnicity')

### Weekly Dataset by Zipcode

df_loc = pd.read_csv('COVID-19_Cases__Tests__and_Deaths_by_ZIP_Code.csv')
df_loc.head()
df_loc.info()
df_loc.isna().sum()

##Data Cleaning

#Lat and Long Cleaning

def clean_zips(df,col):
    lat = []
    long = []
    for row in df[col]:
        try:
            lat.append(row.split(' ')[1])
            long.append(row.split(' ')[2])
        except:
            # append a missing value to lat
            lat.append(np.NaN)
            # append a missing value to lon
            long.append(np.NaN)
    lat_clean = []
    for item in lat:
        try:
            item = item.replace('(','')
            lat_clean.append(item)
        except:
            item = item
            lat_clean.append(item)
        
    long_clean = []
    for item in long:
        try:
            item = item.replace(')','')
            long_clean.append(item)
        except:
            item = item
            long_clean.append(item)
        
    df['lat'] = lat_clean
    df['long'] = long_clean
    return df


##EDA 
    
df_loc.columns
df_loc.sum()



df_zip= df_loc.pivot_table(index = ['ZIP Code Location','ZIP Code'], values = 'Cases - Cumulative',  aggfunc=max)
df_zip.reset_index(inplace = True)

clean_zips(df_zip,'ZIP Code Location')

len(df_zip['ZIP Code'])
len(df_zip['ZIP Code'].unique())

m = folium.Map(location=[41.8781, -87.6298],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")




for lat, long, cases,zipcode in zip(df_zip['lat'],df_zip['long'],df_zip['Cases - Cumulative'],df_zip['ZIP Code']):
    folium.CircleMarker(
                    location = [long,lat],
                    radius = 100,
                    popup = ('ZIP Code: '+ str(zipcode).capitalize() + '<br>'
                             'Cases: ' + str(cases) + '<br>'
                             'Lat: ' + str(lat) + "<br>"
                             'Long: ' + str(long) + "<br>"),
                    color = 'crimson',
                    fill = True).add_to(m)


m.save('chicago_covid_map.html')

highest_zip = df_zip.sort_values(by = 'Cases - Cumulative', ascending = False)[:1]
lowest_zip = df_zip.sort_values(by = 'Cases - Cumulative', ascending = True)[:1]
print("The ZIP Code {} has the highes amount of COVID19 Cases as of 12/23/2020 with {} Cases".format(str(highest_zip['ZIP Code'].values),str(highest_zip['Cases - Cumulative'].values)))
print("The ZIP Code {} has the highes amount of COVID19 Cases as of 12/23/2020 with {} Cases".format(str(lowest_zip['ZIP Code'].values),str(lowest_zip['Cases - Cumulative'].values)))




















