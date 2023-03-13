import pandas as pd
import pytest

PATH = '../data/Fahrraddiebstahl.csv' 

class DataInspector():
    '''Read and transform initial data, fit model and predict.'''

    def __init__(self, path = PATH) -> None:
        self.path = path

    def read_data(self) -> pd.DataFrame:
        '''Return dict with feature matrix and labels as values.'''
        df = pd.read_csv(self.path, index_col=0, parse_dates=True, encoding = 'unicode_escape')
        return df

    def include_timestamps(self, df) -> pd.DataFrame:
        '''Return DataFrame with time-stamps.'''
        df['Year'] = df.index.year
        df['Month'] = df.index.month
        return df

    def time_parser(self, df, time_parsables):
        '''Parses columns encoded as strings to datetime-objects.'''
        for col in time_parsables:
            df[col] = pd.to_datetime(df[col])
        return df

    def check_unique(self, df, col):
        '''Return unique values of selected columns.'''
        return df['DELIKT'].unique()

