import numpy as np
import pandas as pd
from scipy import stats

class HealthAnalyzer:
    def __init__(self, df):
        self.df = df

    def info_print(self):
        """
        Visar olika typer av info från dataframe (head, info, describe, duplicates)
        """
        display(self.df.head())
        display(self.df.info())
        display(self.df.describe())
        print('Dubblettrader: ',self.df.duplicated().any())
    
    def summery_stats(self, columns):
        """Räknar medelvärde, median, min och max av valda kolumner"""
        return self.df[columns].agg(['mean', 'median', 'min', 'max']).round(2)
    
    def disease_sim(self, column='disease', n=1000):
        """
        Skapar en simulering av sjukdomsfördelning från dataset. 
        Retunerar en Dataframe med antal och andelar
        """
        # Data från orginal-df
        num_sick = self.df[column].sum()                    
        num_healthy =(self.df[column] == 0).sum() 
        share_sick = self.df[column].mean() 
        share_healthy = 1 - share_sick

        # Simulering
        sim_disease = np.random.choice([0, 1], size= n, p=[share_healthy, share_sick])
        num_sick_sim = sim_disease.sum()
        num_healthy_sim = (sim_disease == 0).sum()
        share_sick_sim = sim_disease.mean()
        share_healthy_sim = 1 - share_sick_sim

        # Skapa Dataframe för att jämföra
        results = pd.DataFrame({
            'Kategori': ['Sjuka', 'Friska'],
            'Antal (data)': [num_sick, num_healthy],
            'Antal (sim)': [num_sick_sim, num_healthy_sim],
            'Andel (data, %)': [round(share_sick * 100, 2), round(share_healthy * 100, 2)],
            'Andel (sim, %)': [round(share_sick_sim * 100, 2), round(share_healthy_sim * 100, 2)]
        })
        return results