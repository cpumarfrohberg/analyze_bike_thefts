import pandas as pd
import pytest
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

PATH = './artifacts/Tabla_01_English_Unique_postEDA.csv' #TODO: change path for reading in transforme dataset

WEIGHTS = {0:0.41, 1:0.59}

class DataModeler():
    '''Read and transform initial data, fit model and predict.'''

    def __init__(self, path = PATH) -> None:
        self.path = path

    def prepare_data(self) -> dict:
        '''Return dict with feature matrix and labels as values.'''
        df = pd.read_csv(self.path, index_col=0, parse_dates=True)
        X = df[['LO_Active_Employee_Post3Months', 'LO_Active_Employee_Prior6Months','LO_Active_Employee_Post6Months']] # features selected based on calculation of feature importance in NB 'all features'.
        y = df['Client_Status_Post3Months']
        return {'feature_matrix': X, 'labels': y}

    def include_timestamps(self, df) -> pd.DataFrame:
        '''Return DataFrame with time-stamps.'''
        df['Year'] = df.index.year
        df['Month'] = df.index.month
        return df

    def split_timestamp_data(self, X, y) -> dict:
        '''Return dict consisting of split data (incl. timestamps).'''
        X_train, X_val, y_train, y_val = train_test_split(X, y, random_state = 42)
        X_train_timestamped = self.include_timestamps(X_train)
        X_val_timestamped = self.include_timestamps(X_val)
        return {
            'X_train_fe': X_train_timestamped, 
            'X_val_fe': X_val_timestamped,
            'y_train': y_train,
            'y_val': y_val,
            }

    def model_fit(self, X_train, y_train, weights):
        '''Return fitted Logistic Regression model.'''
        clf_LR = LogisticRegression(class_weight = weights, random_state=42) 
        clf_LR.fit(X_train, y_train)
        return clf_LR

    def predictions(self, fit_model, X):
        '''Return model predictions.'''
        clf = fit_model
        return clf.predict(X)

