import pandas as pd
import seaborn as sns
#import pytest

PATH_INITIAL = './data/Fahrraddiebstahl.csv' 
PATH_SAVEABLE = '../data'
PATH_EXTRACTED = './data'

class BikeThefts():
    '''Read, inspect and transform initial data.'''

    def __init__(self, path = PATH_INITIAL, path_saveable = PATH_SAVEABLE, path_extracted = PATH_EXTRACTED) -> None:
        self.path = path
        self.path_saveable = path_saveable
        self.path_extracted = path_extracted

    def read_initial_data(self) -> pd.DataFrame:
        '''Return DataFrame with feature matrix and labels as values.'''
        df = pd.read_csv(self.path, index_col=0, parse_dates=True, encoding = 'unicode_escape')
        return df

    def read_extracted_data(self, file) -> pd.DataFrame:
        '''Return DataFrame extracted from initial data.'''
        df = pd.read_csv(f'{self.path_extracted}/{file}', encoding = 'unicode_escape')
        return df
    
    def check_unique(self, serie) -> pd.Series:
        '''Return unique values of selected columns.'''
        return serie.unique()

    def include_timestamps(self, df) -> pd.DataFrame:
        '''Return DataFrame with time-stamps.'''
        df['year'] = df.index.year
        df['month'] = df.index.month
        return df

    def time_parser(self, df, time_parsables) -> pd.DataFrame:
        '''Parse columns encoded as strings to datetime-objects.'''
        for col in time_parsables:
            df[col] = pd.to_datetime(df[col])
        return df

    def crime_duration_days(self, df, start, end) -> pd.DataFrame: #use for plotting?
        '''Calculate duration of crime in days.'''
        df['crime_duration_days'] = end - start
        return df
    
    def crime_duration_hours(self, df, start, end) -> pd.DataFrame: #use for plotting?
        '''Calculate duration of crime in hours.'''
        df['crime_duration_hours'] = abs(start - end)
        return df
    
    def plot_categoricals(self, df, ordinate) -> sns:
        return sns.catplot(
        data=df, y=ordinate, kind="count",
        palette="pastel", edgecolor=".6",
    )

    def save_data(self, df, group_by, col_names, file):
        '''Save extracted data locally as csv-file.'''
        bike_thefts_LOR = pd.DataFrame(df.groupby(group_by).size(),
                        columns = [col_names]).reset_index()
        return bike_thefts_LOR.to_csv(f'{self.path_saveable}/{file}.csv')

