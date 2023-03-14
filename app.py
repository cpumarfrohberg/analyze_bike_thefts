from utils import BikeThefts
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

CATS = ['bike_type', 'delict', 'description', 'intent_delict']

bike_thefts = BikeThefts()

@st.cache
def load_data():
    df_initial = bike_thefts.read_initial_data()
    df = bike_thefts.read_extracted_data('bike_thefts_transformed.csv')
    bike_thefts_series_22 = bike_thefts.read_extracted_data('bike_thefts_series_2022.csv')
    bike_thefts_series_23 = bike_thefts.read_extracted_data('bike_thefts_series_2023.csv')
    return df_initial, df, bike_thefts_series_22, bike_thefts_series_23

df_initial, df, bike_thefts_series_22, bike_thefts_series_23 = load_data()

st.title('Bike Thefts in Berlin')

nav = st.sidebar.radio(
    'Please chose one of the following:',
    ['Home', 'EDA', 'Heat Map']
    ) 

if nav == 'Home':
    st.markdown(
    ''' ## Welcome to the Bike Thefts in Berlin page.
    ##### Its main objective is to analyze bike thefts in Berlin during the time period 2022-2023.
    '''
    )
  
if st.checkbox('<- If you are interested to see the initial data made available by \
                   the Police Department in Berlin, click here'):
        st.table(df_initial)

if st.checkbox('<- For checking the transformed data, click here'):
        st.table(df)

if nav == 'EDA':
    st.write('Welcome to the section on Exploratory Data Analysis.')

    if st.checkbox('<- Click here to see the type of delicts.'):
        st.write(bike_thefts.check_unique(df['delict']))

    if st.checkbox('<- Click here to see the time series of bike thefts.'):
        val = st.slider(
            'Filter data using years', 
            min_value = 2022, 
            max_value = 2023
            )
        bike_theft_series = bike_thefts_series_22['bike_theft_count']
        #bike_theft_series = bike_theft_series[bike_theft_series.index >= val]
        st.line_chart(bike_theft_series)

    if st.checkbox('<- Click here for checking the categorical variables'):
        fillable_plots = list()
        for cat in CATS:
            fig, ax = plt.subplots()
            fig = sns.catplot(
                    data=df, y= cat, kind='count',
                    palette='pastel', edgecolor='.6'
            )
            fillable_plots.append(fig)
        for plot in fillable_plots:
           time.sleep(3)
           st.pyplot(plot) 

if nav == 'Heat Map':
    st.markdown(
    ''' #### Welcome to the heat map page.
    '''
    )
    
    st.markdown(
    ''' ##### For heat map per LOR, please select from one of the following options.
    '''
    )
    district = st.selectbox('Please select which district you are interested in', df_initial['LOR'].unique())


    # @st.cache
    # def load_model():
    #     print("loading the model")
    #     with open(MODEL_FILE, "rb") as file_in:
    #         clf_LR = pickle.load(file_in)
    #     return clf_LR
    
    # clf_LR = load_model()

    # col1, col2, col3 = st.columns(3)

    # active_past_6 = col1.number_input(
    #     "Was the Loan Officer employed 6 months ago?", 
    #     min_value = 0,
    #     max_value = 1,
    #     )
    # active_post_3 = col2.number_input(
    #     "Do you expect the Loan Officer to still be employed in 3 months time?", 
    #     min_value = 0,
    #     max_value = 1,
    #     )
    # active_post_6 = col3.number_input(
    #     "Do you expect the Loan Officer to still be employed in 6 months time?", 
    #     min_value = 0,
    #     max_value = 1,
    #     )

    if st.button("End"):
        st.success(f'Thank you for your interest and for stopping by.')

