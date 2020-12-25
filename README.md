# An Exploratory Analysis of COVID-19 Focusing on the City of Chicago

## Overview
This project aims to analyze COVID-19's affect on the City of Chicago through different categories of citizens, such as age groups, gender (if-applicable), and race/ethnicity.  A project of this type can be used to study how a global pandemic affects the groups of citizens of a city like Chicago and if something similar were to happen, we can be better prepared to combat the deadly virus against our most at risk citizens.

Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.

Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.

The best way to prevent and slow down transmission is to be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face.

The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).

## Data Collection

* The two datasets were collected from the [Chicago Data Portal](https://data.cityofchicago.org/)
* The two datasets can be found here:
    * [Daily](https://data.cityofchicago.org/Health-Human-Services/Daily-Chicago-COVID-19-Cases-Deaths-and-Hospitaliz/kxzd-kd6a)
    * [Weekly by ZIP Code](https://data.cityofchicago.org/Health-Human-Services/COVID-19-Cases-Tests-and-Deaths-by-ZIP-Code/yhhz-zm2v/data)

## Methods of Analyzation

* Various graphs were constructed using matplotlib.pyplot, seaborn, and folium.  The most informative visualizations (links below) offer an overview of the numbers Chicago has been facing from the near beginning.  
   * [Chicago COVID Cases from 3/1/2020 to 12/23/2020](https://yiannimercer.github.io/COVID19_Chicago_Analysis/covid_cases.html)  
   * [Chicago COVID Deaths from 3/1/2020 to 12/23/2020](https://yiannimercer.github.io/COVID19_Chicago_Analysis/covid_death.html)  
   * [Chicago COVID Hospitalizations from 3/1/2020 to 12/23/2020](https://yiannimercer.github.io/COVID19_Chicago_Analysis/covid_hospitalization.html)  
   * [COVID Mortality Rate from 3/1/2020 to 12/23/2020](https://yiannimercer.github.io/COVID19_Chicago_Analysis/covid_mortality_rate.html)
      
* Additionally the data required some minor cleaning such as extracting the coordinates of each ZIP Code from a single column and over tidying of the data in order to be plotted with folium.
* Feature Engineering was performed to highlight the Mortatlity Rate of Positive COVID cases (# of Deaths over # of Cases in a single day)
    * The average case-fatality ratio according to John Hopkins University is 1.8% for the United States, which is fairly close to our calculated value of about 2.8%

## Conclusion & Insights
As we already know, there are countless ways the novel Coronavirus has affected the different groups of citizens of a city, however I hope this project has offered some insight as to what groups of individuals have experienced the worst of it.  

As you can from the linked graph below, the Bedford Park neighborhood of Chicago (ZIP: 60629) has the highest number of COVID cases as of 12/23/2020, with 13166 cases, however a much more centralized area of the city (ZIP: 60603) has the smallest number of COVID cases with only 46 cases.  I attribute this to the fact the former has a much less dense population and fewer amount of livable space (homes) in the area.
   *  [Chicago COVID Cases Map by ZIP Code](https://yiannimercer.github.io/COVID19_Chicago_Analysis/chicago_covid_map.html)

* Additionally, please feel free to look through the below visualizations I created and draw your own insights!

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_cases_age.png)  

Not suprising that the majority of positive Coronavirus cases are from individuals whose age range from 18-29, as many people who belong to this group are considering the least at risk relative to older inviduals.  As we know from social media, and my experience in the City of Chicago, younger people have a tendency to push against the new orders and policies that are in place to slow the spread of COVID-19. 

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_cases_ethnicity.png)  

A next step for this project, would be to collect demographics on zipcodes of Chicago and cross check the above results against the ZIP Code Graph we have above. 

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_cases_gender.png)  

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_death_age.png)  

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_death_ethnicity.png)  

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_deaths_gender.png)  

While slightly more individuals who identify as male test positive, a noticeable higher percentage of females actually die due to COVID-19. 

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_hospital_age.png)  

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_hospital_age.png)  

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_hospital_ethnicity.png)  

![alt text](https://github.com/yiannimercer/COVID19_Chicago_Analysis/blob/main/images/covid_hospital_gender.png)  


## Extra
As a test of my visualization ability, I also contracted the below Choropleth map that shows the Global Case Count of COVID19

[COVID-19 World Map](https://yiannimercer.github.io/COVID19_Chicago_Analysis/world_covid.html)
