import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def bivariate_analysis(self,column):
        
        aggregated = self.data.groupby(column)['PremiumToClaimsRatio'].mean().reset_index()
        sorted_data = aggregated.sort_values(by='PremiumToClaimsRatio', ascending=False)
        print(f" Premium to Claims Ratio calculated per {column} :")
        print(sorted_data)
        
        plt.figure(figsize=(12, 6))  # Set figure size
        sns.barplot(x=sorted_data[column], y='PremiumToClaimsRatio', data=sorted_data)
        plt.title(f'Average Premium to Claims Ratio by {column}', fontsize=14)
        plt.xlabel(column, fontsize=10)
        plt.ylabel('Average Premium to Claims Ratio', fontsize=10)