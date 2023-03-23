#app.py

from utils import BikeThefts, AggregateThefts
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pydeck as pdk

CATS = ['bike_type', 'delict', 'description', 'intent_delict']

bike_thefts = BikeThefts()
aggregated_bike_thefts = AggregateThefts()

@st.cache_data
def load_data():
    bike_thefts_data = bike_thefts.read_data('Fahrraddiebstahl')
    bike_thefts_transformed = bike_thefts.read_data('bike_thefts_transformed')
    return bike_thefts_data, bike_thefts_transformed

bike_thefts_data, bike_thefts_transformed = load_data()

st.title('Bike Thefts in Berlin')

nav = st.sidebar.radio(
    'Please chose one of the following:',
    ['Home', 'Categorical Variables', 'Numeric Variables', 'Time Series', 'Heat Maps']
    ) 

if nav == 'Home':
    st.markdown(
    ''' ## Welcome to the Bike Thefts in Berlin page.
    ##### Its main objective is to analyze bike thefts in Berlin during the time period 2022-2023.
    '''
    )
  
    if st.checkbox('<- If you are interested to see the initial data made available by \
                    the Police Department in Berlin, click here'):
            st.table(bike_thefts_data)

    if st.checkbox('<- For checking the transformed data, click here'):
            st.table(bike_thefts_transformed)

if nav == 'Categorical Variables':
    st.write('Welcome to the section on Categorical Variables.')
    if st.checkbox('<- Click here for plots on categorical variables'):
        fillable_plots = list()
        for cat in CATS:
            fig, ax = plt.subplots(figsize = (5,3))
            fig = sns.catplot(
                    data=bike_thefts_transformed, y= cat, kind='count',
                    palette='pastel', edgecolor='.6'
            )
            fillable_plots.append(fig)
        for plot in fillable_plots:
           time.sleep(3)
           st.pyplot(plot) 
    
if nav == 'Numeric Variables':
    st.write('Welcome to the section on Numeric Variables.')
    if st.checkbox('<- Click here for checking a box plot'):
        multi_biketype_month = bike_thefts_transformed.groupby(['bike_type', 'year'])['damage_amount'].mean()
        multi_biketype_month = multi_biketype_month.unstack().round(2)
        multi_biketype_month = multi_biketype_month.reset_index()
        multi_biketype_month_long = multi_biketype_month.melt(id_vars='bike_type', var_name='year', value_name='bike_thefts')
        fig, ax = plt.subplots(figsize = (5,3))
        sns.boxplot(x='year', y='bike_thefts', data=multi_biketype_month_long)
        st.pyplot(fig)

    if st.checkbox('<- Click here for seeing the mean damage amount district'):
        mean_damage_by_district = aggregated_bike_thefts.mean_vals(bike_thefts_transformed, 'district', 'damage_amount')
        mean_damage_by_district = round(mean_damage_by_district, 0)
        mean_damage_by_district.set_index('district', inplace = True)
        st.bar_chart(mean_damage_by_district)
    
    if st.checkbox('<- Click here for seeing the number of bike thefts by district'):
        thefts_by_district = aggregated_bike_thefts.aggregate_thefts(bike_thefts_transformed, 'district')
        thefts_by_district.rename(columns={0:'number_bike_thefts'}, inplace=True)
        thefts_by_district.set_index('district', inplace=True)
        thefts_by_district.sort_values(by = 'number_bike_thefts', ascending=False, inplace=True)
        st.bar_chart(thefts_by_district)

if nav == 'Time Series':
    st.write('Welcome to the section on Time Series.')

    if st.checkbox('<- Click here to see the daily values of bike thefts.'):
        bike_theft_series = bike_thefts_transformed.loc['2022-01-02':'2023-02-19'].resample('D').size()
        st.line_chart(bike_theft_series) 
    
    if st.checkbox('<- Click here to see the weekly values of bike thefts.'):
        bike_theft_series = bike_thefts_transformed.loc['2022-01-02':'2023-02-19'].resample('W').size()
        st.line_chart(bike_theft_series) 

if nav == 'Heat Maps':
    st.markdown(
    ''' #### Welcome to the heat map page.
    '''
    )
      
    if st.checkbox('Click here to see the how variables are correlated with each other (pearson).'):
        corr = bike_thefts_transformed.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, ax=ax)
        st.write(fig)
    
   
    if st.checkbox('Click here to see geodata being plotted.'):
        layer = pdk.Layer(
        'ScatterplotLayer',
        data=bike_thefts_transformed,
        get_position='[lon, lat]',
        get_color='[200, 30, 0, 160]',
        get_radius=1000,
    )

    view_state = pdk.ViewState(
        longitude=13.4,
        latitude=52.5,
        zoom=11,
        pitch=50
    )

    # map = pdk.Deck(
    #     layers=[layer],
    #     initial_view_state=view_state,
    # )
   
    # st.pydeck_chart(map)

    # st.markdown(
    # ''' ##### For heat map per LOR, please select from one of the following options.
    # '''
    # )
    
    
    # #district = st.selectbox('Please select which district you are interested in', bike_thefts_transformed['LOR'].unique())

    # if st.button("End"):
    #     st.success(f'Thank you for your interest and for stopping by.')

