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
        
        plt.figure(figsize=(14, 8))  # Set figure size
        sns.barplot(x=sorted_data[column], y='PremiumToClaimsRatio', data=sorted_data)
        plt.title(f'Average Premium to Claims Ratio by {column}', fontsize=12)
        plt.xlabel(column, fontsize=10)
        plt.ylabel('Average Premium to Claims Ratio', fontsize=10)

    def geographical(self):

        aggregated = self.data.groupby(['Province','CoverType']).size().reset_index(name='count')
        sorted_data = aggregated.sort_values(by='count', ascending=False)
        print(f" Cover type per province")
        print(sorted_data)
        
    def multivariate_analysis(self):
        column = ['Province','Gender']
        aggregated = self.data.groupby(column)['PremiumToClaimsRatio'].mean().reset_index()
        sorted_data = aggregated.sort_values(by='PremiumToClaimsRatio', ascending=False)
        print(f" Premium to Claims Ratio calculated per {column} :")
        print(sorted_data)
        
        plt.figure(figsize=(12, 6))  # Set figure size
        sns.scatterplot(x=sorted_data['Gender'], y=sorted_data['PremiumToClaimsRatio'], hue=sorted_data['Province'],
                        data=sorted_data)
        plt.title(f'Average Premium to Claims Ratio by {column}', fontsize=12)
        plt.xlabel(column, fontsize=10)
        plt.ylabel('Average Premium to Claims Ratio', fontsize=10)

    def multivariate_analysis_2(self):
        column = ['Province','MaritalStatus']
        aggregated = self.data.groupby(column)['PremiumToClaimsRatio'].mean().reset_index()
        sorted_data = aggregated.sort_values(by='PremiumToClaimsRatio', ascending=False)
        print(f" Premium to Claims Ratio calculated per {column} :")
        print(sorted_data)
        
        plt.figure(figsize=(12, 6))  # Set figure size
        sns.scatterplot(x=sorted_data['MaritalStatus'], y=sorted_data['PremiumToClaimsRatio'], hue=sorted_data['Province'],
                        data=sorted_data)
        plt.title(f'Average Premium to Claims Ratio by {column}', fontsize=12)
        plt.xlabel(column, fontsize=10)
        plt.ylabel('Average Premium to Claims Ratio', fontsize=10)

    def time_analysis(self):
        self.data['TransactionMonth'] = pd.to_datetime(self.data['TransactionMonth'], format='%Y-%m')
        plt.figure(figsize=(14, 7))
        plt.plot(self.data.groupby('TransactionMonth')['TotalPremium'].mean(), label='Average Total Premium')
        plt.plot(self.data.groupby('TransactionMonth')['TotalClaims'].mean(), label='Average Total Claims')
        plt.title('Trends Over Time')
        plt.xlabel('Month')
        plt.ylabel('Value')
        plt.legend()
        plt.show()
