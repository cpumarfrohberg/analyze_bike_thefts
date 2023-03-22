#transform.py
'''Transform initial data and extract DataFrames for plotting.'''
from utils import BikeThefts, TIME_PARSEABLE, DISTRICT_DICT

import pandas as pd
import numpy as np
import logging
import time

logging.basicConfig(level = logging.INFO)

import warnings
warnings.filterwarnings('ignore')

def main():
    bike_thefts = BikeThefts()
    time.sleep(2)
    logging.info('reading data')
    df = bike_thefts.read_data('Fahrraddiebstahl')
    time.sleep(2)
    logging.info('renaming cols')
    df = bike_thefts.rename_cols(df)
    time.sleep(2)
    logging.info('parsing time')
    df_transformed = bike_thefts.time_parser(df, TIME_PARSEABLE)
    df_transformed = bike_thefts.crime_duration_minutes(df_transformed, 
                                            start_time = df_transformed['start_time_delict'], 
                                            end_time = df_transformed['end_time_delict'])
    df_transformed = bike_thefts.include_timestamps(df_transformed)
    time.sleep(2)
    logging.info('extracting district names')
    df_transformed = bike_thefts.insert_district(df_transformed, DISTRICT_DICT)
    time.sleep(2)
    logging.info('saving transformed dataset')
    bike_thefts.save_intermediate_data(df_transformed, 'bike_thefts_transformed') # save complete transformed dataset
    
if __name__ == '__main__':
    main()