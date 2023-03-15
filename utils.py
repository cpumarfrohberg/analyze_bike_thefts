import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#import pytest

PATH = './data' #note difference to notebook, which is in EDA-dir

time_parseable = ['start_date_delict', 'end_date_delict']

class BikeThefts():
    '''Read, inspect and transform initial data.'''

    def __init__(self, path = PATH) -> None:
        self.path = path

    def read_initial_data(self, file) -> pd.DataFrame:
        '''Return DataFrame with feature matrix and labels as values.'''
        df = pd.read_csv(f'{self.path}/{file}', index_col=0, parse_dates=True, encoding = 'unicode_escape')
        return df

    def read_extracted_data(self, file) -> pd.DataFrame:
        '''Return DataFrame extracted from initial data.'''
        df = pd.read_csv(f'{self.path}/{file}', encoding = 'unicode_escape')
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
    
    def fill_ints(self, df) -> pd.DataFrame:
        '''Reencode LOR into 8-digit values.'''
        df['LOR'] = df['LOR'].apply(lambda x: str(x))
        df['LOR'] = df['LOR'].apply(lambda x: f'0{(x)}'[-8:])
        return df
    
    def fill_ints_grouped(self, df) -> pd.DataFrame:
        '''Group by LOR. Return df including number of bike thefts per LOR-group.'''
        df_grouped = pd.DataFrame(df.groupby('LOR').size(),
                          columns=['bike_thefts']).reset_index()
        return df_grouped
        
    def rename_cols(self, df) -> pd.DataFrame:
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
    
    def save_intermediate_data(self, df, file: str):
        '''Save extracted data locally as csv-file.'''
        return df.to_csv(f'{self.path}/{file}.csv')

    def save_LOR_bike_thefts(self, df, group_by: str, col_names: str, file: str):
        '''Save extracted LOR-bike thefts-data locally as csv-file.'''
        bike_thefts_LOR = pd.DataFrame(df.groupby(group_by).size(),
                        columns = [col_names]).reset_index()
        return bike_thefts_LOR.to_csv(f'{self.path}/{file}.csv')

    class PlotBikeThefts():
        '''Plot data with seaborn.'''

    def plot_categoricals(self, df, ordinate) -> sns:
            return sns.catplot(
            data=df, y=ordinate, kind="count",
            palette="pastel", edgecolor=".6",
        )

    def plot_correlations(self, df) -> sns:
        corr = df.corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        f, ax = plt.subplots(figsize=(8, 6))
        plt.xticks(rotation=45)
        cmap = sns.diverging_palette(230, 20, as_cmap=True)
        return sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                    square=True, linewidths=.5, cbar_kws={"shrink": .5})
    

    # def reencode_LOR(self, df, dictionary) -> pd.DataFrame:
    #     '''Reencode LOR into name of district.'''
    #     for idx, row in df['LOR'].items():
    #         for key in dictionary.keys():
    #             if key in row[0:2]:
    #                 row = dictionary[key]
    #             else:
    #                 continue
    #         return df