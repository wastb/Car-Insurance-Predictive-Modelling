import pandas as pd
import os

def load_data(path):
    """
    Load data from a CSV file into a pandas DataFrame.

    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(
            path,
            dtype={37: object},              
            na_values=['NA', 'null', ' ','  ', '']    #treat blanks as missing values
        )
        print("Data Loaded Successfully")
        return df

    except Exception as e:
        print(f"Data extraction unsuccessful: {e}")

    return None

    
         
