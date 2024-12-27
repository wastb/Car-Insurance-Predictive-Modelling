import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DataPreprocessing:
    def __init__(self, data):
        self.data = data


    def to_datetime(self):
        """
        Convert Column data types to date time.
        """
        self.data['TransactionMonth'] = pd.to_datetime(self.data['TransactionMonth'], errors='coerce')
        self.data['VehicleIntroDate'] = pd.to_datetime(self.data['VehicleIntroDate'], errors='coerce')

    
    def drop_columns(self):
        """ 
        Drop columns that are not necessary for the analysis.This columns doesn't offer anything to the analysis since they only
        contain a single value over their entire column or They are not relevant to provide insight"""

        columns_to_drop = ['Language','Country','ItemType','CrossBorder','NumberOfVehiclesInFleet',
                         'StatutoryClass','StatutoryRiskType', 'Model', 'Cylinders', 'cubiccapacity', 
                         'VehicleIntroDate','kilowatts','Bank','AccountType','mmcode','Title','VehicleIntroDate',
                         'CustomValueEstimate','CapitalOutstanding','WrittenOff','Rebuilt','Converted']
        
        self.data.drop(columns=columns_to_drop, inplace=True)

    
    def categorical_plot_1(self):
        categorical_columns = ['IsVATRegistered','Citizenship','Province','VehicleType','Gender',
                               'AlarmImmobiliser']

        plt.figure(figsize=(12,10))
        for i,col in enumerate(categorical_columns):
            plt.subplot(2, 3, i + 1)
            self.data[col].value_counts().plot(kind='bar')
            plt.title(col)
            plt.xlabel('Value')
            plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()
        
    def categorical_plot_2(self):
        categorical_columns_2 = ['LegalType','MainCrestaZone','bodytype','NewVehicle','TrackingDevice','TermFrequency']
        
        plt.figure(figsize=(12,10))
        for i,col in enumerate(categorical_columns_2):
            plt.subplot(2, 3, i + 1)
            self.data[col].value_counts().plot(kind='bar')
            plt.title(col)
            plt.xlabel('Value')
            plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()
        
    def categorical_plot_3(self):
        categorical_columns_3 = ['MaritalStatus','CoverGroup', 'Section', 'Product']
        
        plt.figure(figsize=(12,10))
        for i,col in enumerate(categorical_columns_3):
            plt.subplot(2, 2, i + 1)
            self.data[col].value_counts().plot(kind='bar')
            plt.title(col)
            plt.xlabel('Value')
            plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()

    def numerical_dist(self):
        columns = ['TotalClaims','TotalPremium','CalculatedPremiumPerTerm','NumberOfDoors']

        plt.figure(figsize=(12,6))
        for i,col in enumerate(columns):
            plt.subplot(2, 2, i + 1)
            plt.hist(self.data[col], bins=20)
            plt.title(col)
            plt.xlabel('Value')
            plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()

    def handle_missing_values(self):
        """
        Fill missing values with mode
        """
        columns = ['Gender','MaritalStatus','VehicleType','NumberOfDoors','bodytype',
                    'NewVehicle','bodytype','make','Citizenship']
        for col in columns:
            mode = self.data[col].mode()[0]
            self.data[col] = self.data[col].fillna(mode)

        return self.data

    def outlier_detection(self):
        outlier_columns = ['TotalPremium','TotalClaims']

        plt.figure(figsize=(12,8))
        for i,col in enumerate(outlier_columns):
            plt.subplot(2, 2, i + 1)
            plt.boxplot(self.data[col])
            plt.title(col)
            plt.xlabel('Value')
            plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()

    def handle_outliers(self):
        # Compute Q1 (25th percentile) and Q3 (75th percentile)
        column = ['TotalPremium','TotalClaims']
        Q1 = self.data[column].quantile(0.25)
        Q3 = self.data[column].quantile(0.75)
        
        # Calculate the IQR
        IQR = Q3 - Q1
        
        # Define lower and upper bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        self.data[column] = np.where(self.data[column] < lower_bound, lower_bound, self.data[column])
        self.data[column] = np.where(self.data[column] > upper_bound, upper_bound, self.data[column])
        
        return self.data

    

        

