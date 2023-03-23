#utils.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


PATH = './data'

DISTRICT_DICT = {
    '01': 'Mitte',
    '02': 'Friedrichshain-Kreuzberg',
    '03': 'Pankow',
    '04': 'Charlottenburg-Wilmersdorf',
    '05': 'Spandau',
    '06': 'Steglitz-Zehlendorf',
    '07': 'Tempelhof-Schöneberg',
    '08': 'Neukölln',
    '09': 'Treptow-Köpenick',
    '10': 'Marzahn-Hellersdorf',
    '11': 'Lichtenberg',
    '12': 'Reinickendorf',
    }

TIME_PARSEABLE = ['start_date_delict', 'end_date_delict', 'start_time_delict', 'end_time_delict']

class BikeThefts():
    '''Read, inspect and transform initial data.'''

    def __init__(self, path = PATH) -> None:
        self.path = path

    def read_data(self, file: str) -> pd.DataFrame:
        '''Return DataFrame with feature matrix and labels as values.'''
        df = pd.read_csv(f'{self.path}/{file}.csv', index_col=0, parse_dates=True, encoding = 'unicode_escape')
        return df

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
    
    def crime_duration_minutes(self, df: pd.DataFrame, start_time: pd.Series, end_time: pd.Series) -> pd.DataFrame:
        '''Calculate duration of crime in hours.'''
        df['time_diff'] = end_time.sub(start_time).dt.total_seconds().div(60)
        return df 
    
    def insert_district(self, df, dictionary):
        '''Iterate thru rows of LOR-column and parse values into district names.
        Insert district names into a new column, "districts".'''
        for idx,row in df.loc[:, ['LOR']].iterrows():
            lor_as_string = str(row[0])
            if len(lor_as_string) < 8:
                lor_as_string = "0"+lor_as_string
            starting_letters=lor_as_string[0:2]
            if starting_letters in dictionary:
                df.loc[idx, 'district'] = dictionary[starting_letters]
            else:
                continue
        return df
      
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
    
class AggregateThefts():
        '''Analyze data by aggregating by different vals.'''
        
        def aggregate_thefts(self, df: pd.DataFrame, group_variable:str) -> pd.DataFrame:
                '''Calculate aggregated vals per group variable and aggregation variable.'''
                df_filled = df.groupby([group_variable]).size()
                df_filled = pd.DataFrame(df_filled).reset_index()
                return df_filled
        
        def mean_vals(self, df: pd.DataFrame, group_variable:str, aggregate_variable:str) -> pd.DataFrame:
                '''Calculate mean vals per group variable and aggregation variable.'''
                df_filled = df.groupby([group_variable])[aggregate_variable].mean()
                df_filled = pd.DataFrame(df_filled).reset_index().sort_values(by = aggregate_variable, ascending=False)
                return df_filled