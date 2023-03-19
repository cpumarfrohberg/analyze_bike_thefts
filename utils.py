import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#import pytest

#TODO; import type hints from refactor
#TODO; clarify what .mean_thefts() does

PATH = './data'

TIME_PARSEABLE = ['start_date_delict', 'end_date_delict', 'start_time_delict', 'end_time_delict']

class BikeThefts():
    '''Read, inspect and transform initial data.'''

    def __init__(self, path = PATH) -> None:
        self.path = path

    def read_data(self, file: str) -> pd.DataFrame:
        '''Return DataFrame with feature matrix and labels as values.'''
        df = pd.read_csv(f'{self.path}/{file}.csv', index_col=0, parse_dates=True, encoding = 'unicode_escape')
        return df
    
    def check_unique(self, series: pd.Series) -> pd.Series:
        '''Return unique values of selected columns.'''
        return series.unique()

    def include_timestamps(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Return DataFrame with time-stamps.'''
        df['hour'] = df.index.hour
        df['day'] = df.index.day
        df['week_day'] = df.index.weekday
        df['week'] = df.index.week
        df['year'] = df.index.year
        df['month'] = df.index.month
        return df

    def time_parser(self, df: pd.DataFrame, time_parsables: list) -> pd.DataFrame:
        '''Parse columns encoded as strings to datetime-objects.'''
        for col in time_parsables:
            df[col] = pd.to_datetime(df[col])
        return df

    def crime_duration_days(self, df: pd.DataFrame, start, end) -> pd.DataFrame: #use for plotting?
        '''Calculate duration of crime in days.'''
        df['crime_duration_days'] = end - start
        return df #check if you want to keep it 
    
    def crime_duration_hours(self, df: pd.DataFrame, start, end) -> pd.DataFrame: #use for plotting?
        '''Calculate duration of crime in hours.'''
        df['crime_duration_hours'] = abs(start - end)
        return df #check if you want to keep it 
    
    def fill_ints(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Reencode LOR into 8-digit values.'''
        df['LOR'] = df['LOR'].apply(lambda x: str(x))
        df['LOR'] = df['LOR'].apply(lambda x: f'0{(x)}'[-8:])
        return df

    def thefts_count(self, df: pd.DataFrame, frequency:str) -> pd.DataFrame:
        '''Calculate average thefts per time-frequency.'''
        df_filled = pd.DataFrame(df.groupby(frequency).size(),
                          columns=[f'{frequency}_thefts_count']).reset_index()
        return df_filled
    
    def mean_thefts(self, df: pd.DataFrame, group_variable:str, aggregate_variable:str) -> pd.DataFrame:
        '''Calculate average thefts per group_variable and aggregate_variable.'''
        df_filled = pd.DataFrame(df.groupby(group_variable)[aggregate_variable].mean(),
                          columns=[f'{aggregate_variable}_average_thefts']).reset_index()
        return df_filled
      
    def rename_cols(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.rename(columns={ 
            'ANGELEGT_AM' : 'track_date',
            'TATZEIT_ANFANG_DATUM' : 'start_date_delict',
            'TATZEIT_ANFANG_STUNDE' : 'start_time_delict',
            'TATZEIT_ENDE_DATUM' : 'end_date_delict',
            'TATZEIT_ENDE_STUNDE' : 'end_time_delict',
            'SCHADENSHOEHE' : 'damage_amount',
            'VERSUCH' : 'intent_delict',
            'ART_DES_FAHRRADS' : 'bike_type',
            'DELIKT' : 'delict',
            'ERFASSUNGSGRUND' : 'description'
            })
    
    def save_intermediate_data(self, df: pd.DataFrame, file: str):
        '''Save extracted data locally as csv-file.'''
        return df.to_csv(f'{self.path}/{file}.csv')

    def save_LOR_bike_thefts(self, df, group_by: str, col_names: str, file: str):
        '''Save extracted LOR-bike thefts-data locally as csv-file.'''
        bike_thefts_LOR = pd.DataFrame(df.groupby(group_by).size(),
                        columns = [col_names]).reset_index()
        return bike_thefts_LOR.to_csv(f'{self.path}/{file}.csv') #necessary?
    
    #TODO; include class for plotting time series?