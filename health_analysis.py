import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Fick vågor under alla 'display' så rådfrågade min vän ChatGPT som hänvisade till att importra nedan.
from IPython.display import display  


class HealthAnalyzer:
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Tar in dataframe som underlag av analyser
        """
        self.df = df

    def info_print(self) -> None:
        """
        Visar olika typer av info från dataframe (head, info, describe, duplicates)
        """
        display(self.df.head())
        display(self.df.info())
        display(self.df.describe())
        print('Dubblettrader: ',self.df.duplicated().any())
    
    def summery_stats(self, columns: list) -> pd.DataFrame:
        """Räknar medelvärde, median, min och max av valda kolumner"""
        return self.df[columns].agg(['mean', 'median', 'min', 'max']).round(2)
    
    def disease_sim(self, column: str ='disease', n: int =1000) -> pd.DataFrame:
        """
        Skapar en simulering av sjukdomsfördelning från dataset. 
        Retunerar en Dataframe med antal och andelar från både orginaldata och simulering
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
    
    def linear_regression(self, x_cols: list, y_col: str) -> dict:
        """
        Tar ut värden för en linjär regression (både enkel och multipel) 
        Retunerar dict med: intercept, slope, R2
        """
        X = self.df[x_cols].values
        y = self.df[y_col].values

        model = LinearRegression()
        model.fit(X, y)

        return {
            'intercept': float(model.intercept_),
            'slope' : model.coef_,
            'R2' : float(model.score(X, y))
        }
    
class Plotter:
    def bar(self, ax, x: list, y:list, title:str, xlabel:str, ylabel:str, alpha: float=1.0):
        """Bar-diagram"""
        ax.bar(x, y)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True, axis= 'y')
        return ax
    
    def box(self, ax, df: pd.DataFrame, column: str , by: str , title: str, xlabel: str, ylabel: str):
        """Boxplot column = kolumn som ska plottas, by = kolumn för gruppering"""
        df.boxplot(column=column, by=by, ax=ax)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True, axis= 'y')
        plt.suptitle('')        #Ta bort auto-titel
        return ax
    
    def scatter(self, ax, x: list, y: list, title: str, xlabel: str, ylabel: str, alpha: float=0.6):
        """Scatter-diagram"""
        ax.scatter(x, y)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True, axis='both')        
        return ax
    
    def hist(self, ax, data: list, title: str, xlabel: str, ylabel: str,bins: int =20, alpha: float=0.7, edgecolor=None):
        """Histogram"""
        ax.hist(data, bins=bins, alpha=alpha, edgecolor=edgecolor)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True, axis= 'y')
        return ax
    
    def plot(self, ax, x, y, color='black', linewidth=2, label=''):
        ax.plot(x, y, color=color, linewidth=linewidth, label=label)
       