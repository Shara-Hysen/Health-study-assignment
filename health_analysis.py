import numpy as np
import pandas as pd
from scipy import stats

class HealtAnalyzer:
    def __init__(self, df):
        self.df = df

    def info_print(self):
        """Visar olika typer av info från dataframe (head, info, describe, duplicates)"""
        display(self.df.head())
        display(self.df.info())
        display(self.df.describe())
        print('Dubblettrader: ',self.df.duplicated().any())
    
    def summery_stats(self, columns):
        """Räknar medelvärde, median, min och max av valda kolumner"""
        return self.df[columns].agg(['mean', 'median', 'min', 'max']).round(2)