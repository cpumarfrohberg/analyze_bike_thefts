#transform.py
'''Transform initial data and extract DataFrames for plotting.'''
from utils import BikeThefts, TIME_PARSEABLE

import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

def main():
    bike_thefts = BikeThefts()
    df = bike_thefts.read_data('Fahrraddiebstahl')
    df = bike_thefts.rename_cols(df)
    df_transformed = bike_thefts.time_parser(df, TIME_PARSEABLE)
    df_transformed = bike_thefts.crime_duration_days(df_transformed, 
                                            start=df_transformed['start_date_delict'], 
                                            end = df_transformed['end_date_delict'])
    df_transformed = bike_thefts.crime_duration_hours(df_transformed, 
                                            start=df_transformed['start_time_delict'], 
                                            end = df_transformed['end_time_delict'])
    df_transformed = bike_thefts.include_timestamps(df_transformed)
    df_transformed = bike_thefts.fill_ints(df_transformed)
    mean_damage_amount = bike_thefts.mean_thefts(df_transformed, 'bike_type', 'damage_amount')
    bike_thefts.save_intermediate_data(df_transformed, 'bike_thefts_transformed') # save complete transformed dataset
    bike_thefts.save_intermediate_data(mean_damage_amount, 'mean_damage_amount') # save grouped vals for plotting
    
if __name__ == '__main__':
    main()