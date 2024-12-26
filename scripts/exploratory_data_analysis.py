import pandas as pd
import matplotlib.pyplot as plt


class exploratoryDataAnalysis:
    def __init__(self,data):
        self.data = data

    
    def to_datetime(self):
        self.data['TransactionMonth'] = pd.to_datetime(self.data['TransactionMonth'], errors='coerce')
        self.data['VehicleIntroDate'] = pd.to_datetime(self.data['VehicleIntroDate'], errors='coerce')

        return self.data

      



    

        

