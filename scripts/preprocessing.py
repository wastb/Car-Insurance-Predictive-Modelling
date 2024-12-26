import pandas as pd
import matplotlib.pyplot as plt


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
                         'CustomValueEstimate','CapitalOutstanding']
        
        self.data.drop(columns=columns_to_drop, inplace=True)

      



    

        

